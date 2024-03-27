from application import app
from application.services.battery_service.battery_service import BatteryService
from flask import request,render_template



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def directory_submit():
    text = request.form['textInput']
    processed_text = text.lower()

    directory = "application/datafiles/"+processed_text+".csv"
    battery_service = BatteryService()

    preprocess_message = battery_service.pre_processer_battery(directory=directory)

    unique_id_creator_message, unique_names_list = battery_service.unique_id_finder_battery(directory=directory)

    unique_dealer_creator_message = battery_service.unique_dealer_finder_battery(directory=directory)

    unique_year_creator_message = battery_service.unique_year_finder_battery(directory=directory)

    return render_template('index.html',
                           processed_text=processed_text,
                           preprocess_message=preprocess_message,
                           unique_id_creator_message=unique_id_creator_message,
                           unique_names_list=unique_names_list,
                           unique_dealer_creator_message=unique_dealer_creator_message,
                           unique_year_creator_message=unique_year_creator_message)