import os
import pandas as pd
from flask import request, render_template, redirect, url_for, session, send_file
from werkzeug.utils import secure_filename
from application import app
from application.securefiles.secretkey import SESSION_ENABLE_KEY
from application.services.battery_service.battery_service import BatteryService

# Set the secret key for session management
app.secret_key = SESSION_ENABLE_KEY

# Configure a temporary directory for storing DataFrame files
app.config['TEMP_DIR'] = os.path.join(os.path.dirname(__file__), 'datafiles', 'temporary_dataframe')



@app.route('/')
def index():
    file_path = session.get('file_path', None)
    preprocessing_flag = 'df_filename' in session
    preprocess_message = session.get('preprocess_message', '')
    table_head = session.get('table_head', '')
    table_tail = session.get('table_tail', '')
    number_of_ids = session.get('number_of_ids', None)

    return render_template('index.html',
                           file_path=file_path,
                           preprocessing_flag=preprocessing_flag,
                           preprocess_message=preprocess_message,
                           table_head=table_head,
                           table_tail=table_tail,
                           number_of_ids=number_of_ids)


@app.route('/', methods=['POST'])
def file_submit():
    if 'fileInput' not in request.files:
        return 'No file part'

    file = request.files['fileInput']

    if file.filename == '':
        return 'No selected file'

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['TEMP_DIR'], filename)
        file.save(file_path)

        session['file_path'] = file_path

        battery_service = BatteryService()
        preprocess_message, df = battery_service.pre_processer_battery(file)
        print(f"Preprocess Message: {preprocess_message}")  # Debug output
        unique_id_creator_message, unique_names_list, number_of_unique_ids = battery_service.unique_id_finder_battery(file)

        # Store preprocessing results in session
        session['preprocess_message'] = preprocess_message
        session['table_head'] = df.head().to_html(classes='table table-striped', index=False)
        session['table_tail'] = df.tail().to_html(classes='table table-striped', index=False)
        session['df_filename'] = os.path.join(app.config['TEMP_DIR'], f'{filename}.pkl')
        session['number_of_ids'] = number_of_unique_ids

        # Save DataFrame as pickle file
        df.to_pickle(session['df_filename'])

        return redirect(url_for('index'))

    return redirect(url_for('index'))


@app.route('/add_data', methods=['POST'])
def add_data():
    # Get form data
    data = {
        'Month': request.form['month'],
        'Year': request.form['year'],
        'Dealer Code': request.form['dealer_code'],
        'Dealer': request.form['dealer'],
        'Item ID': request.form['item_id'],
        'Item name': request.form['item_name'],
        'Segment': request.form['segment'],
        'District': request.form['district'],
        'Sales Value': request.form['sales_value'],
        'Sales Quantity': request.form['sales_quantity']
    }

    # Get file path from session
    csv_path = session.get('file_path', None)

    if csv_path:
        # Call the add_data method from BatteryService
        battery_service = BatteryService()
        if battery_service.add_data(data, csv_path):
            # Increment the count
            number_of_ids = session.get('number_of_ids', 0)
            session['number_of_ids'] = number_of_ids + 1

            # Refresh table data
            df = pd.read_csv(csv_path)
            session['table_head'] = df.head().to_html(classes='table table-striped', index=False)
            session['table_tail'] = df.tail().to_html(classes='table table-striped', index=False)
            session['df_filename'] = os.path.join(app.config['TEMP_DIR'], f'{os.path.basename(csv_path)}.pkl')
            df.to_pickle(session['df_filename'])
    return redirect(url_for('index'))



@app.route('/product')
def product():
    df_filename = session.get('df_filename', None)

    if df_filename is None:
        return "No data frame found. Please upload a file first."

    # Load DataFrame from file storage
    df = pd.read_pickle(df_filename)
    df_preview = df.head(10).to_html(classes='table table-striped', index=False)

    return render_template('product.html', table_preview=df_preview)


@app.route('/download_csv', methods=['GET'])
def download_csv():
    df_filename = session.get('df_filename', None)

    if df_filename is None:
        return "No data frame found. Please upload a file first."

    try:
        df = pd.read_pickle(df_filename)

        # Temporarily save the DataFrame to a CSV file
        temp_csv_path = os.path.join(app.config['TEMP_DIR'], 'temp_download.csv')
        df.to_csv(temp_csv_path, index=False)

        # Send the CSV file as response
        return send_file(temp_csv_path, as_attachment=True, download_name='updated_data.csv')

    except Exception as e:
        return str(e)




@app.route('/dealer')
def dealer():
    return render_template('dealer.html')

@app.route('/plots')
def plots():
    return render_template('plots.html')


@app.route('/forecast')
def forecast():
    return render_template('forecast.html')


@app.route('/extra_features')
def extra_features():
    return render_template('extra_features.html')


