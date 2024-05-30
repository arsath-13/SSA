import pandas as pd
from io import StringIO
import os
import re

class BatteryRepository:

    def pre_processor_battery(self, file):
        try:
            # Check if the file is already a CSV
            if file.filename.endswith('.csv'):
                file.seek(0)  # Move to the start of the file
                df = pd.read_csv(file)
            elif file.filename.endswith('.xlsx'):
                file.seek(0)  # Move to the start of the file
                df = pd.read_excel(file, engine='openpyxl')
            elif file.filename.endswith('.xls'):
                file.seek(0)  # Move to the start of the file
                df = pd.read_excel(file, engine='xlrd')
            else:
                raise ValueError("Unsupported file format. Please upload a CSV or Excel file.")

            # Log the contents of the dataframe
            print("DataFrame content:\n", df.head())

            # Preprocess the DataFrame
            if df.empty:
                raise ValueError("The uploaded file is empty or does not contain any columns.")

            df.dropna(inplace=True)
            if 'ITEMID' in df.columns:
                df.rename(columns={'ITEMID': 'Item ID'}, inplace=True)
            else:
                print("Required column 'ITEMID' not found in the file.")

            # Save the DataFrame back to a CSV (temporary saving for session use)
            csv_buffer = StringIO()
            df.to_csv(csv_buffer, index=False)
            preprocess_message = "Data file is uploaded successfully."
            print(preprocess_message)
            return preprocess_message, df

        except Exception as e:
            preprocess_message = f"Error in uploading the data file: {e}"
            print(preprocess_message)
            return preprocess_message, None

    def unique_id_finder_battery(self, file):
        try:
            # Read the CSV file from the file object
            file.seek(0)  # Move to the start of the file
            df = pd.read_csv(file)
            unique_ids_list = df['Item ID'].unique()
            unique_names_list = df['Item name'].unique()
            number_of_unique_ids = len(unique_ids_list)
            sorted_unique_names_list = sorted(unique_names_list)
            folder_path = 'application/datafiles/unique_id_data_files'

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            for every_item_id in unique_ids_list:
                item_data = df[df['Item ID'] == every_item_id]
                sanitized_item_id = re.sub(r'[^\w\-_. ]', '', str(every_item_id))
                filename = os.path.join(folder_path, f'{sanitized_item_id}.csv')
                item_data.to_csv(filename, index=False)

            unique_id_creator_message = "Unique data files based on Item Id, are created successfully..."
            return unique_id_creator_message, sorted_unique_names_list, number_of_unique_ids

        except FileNotFoundError as e:
            unique_id_creator_message = f"Error in unique id data file creation (Battery): {e}"
            return unique_id_creator_message, None, None

    def add_data(self, data, csv_path):
        try:
            # Create DataFrame with new data
            new_row = pd.DataFrame(data, index=[0])

            # Check if the CSV file exists
            if not os.path.exists(csv_path):
                # If the file doesn't exist, create a new one with the new data
                new_row.to_csv(csv_path, index=False)
            else:
                # If the file exists, append the new data to it
                df = pd.read_csv(csv_path)
                df = pd.concat([df, new_row], ignore_index=True)
                df.to_csv(csv_path, index=False)

            return True

        except Exception as e:
            print(f"Error adding data: {e}")
            return False

    def model_loader(self):
        pass

    def sales_forecasting(self):
        pass