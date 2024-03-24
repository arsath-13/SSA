import pandas as pd
import os
import re

class BatteryRepository:

    def pre_processor_battery(self, directory):
        try:
            df = pd.read_csv(directory)
            df.dropna(inplace=True)
            df.rename(columns={'ITEMID': 'Item ID'}, inplace=True)
            df.to_csv(directory, index=False)
            print("Battery Data file preprocessing is completed successfully")
        except FileNotFoundError as e:
            print("Error in Pre-processing (Battery) : ",e)

    def unique_id_finder_battery(self, directory):
        try:
            df = pd.read_csv(directory)
            unique_ids_list = df['Item ID'].unique()
            folder_path = 'application/datafiles/battery_data_files/unique_battery_id_data_files'

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            for every_item_id in unique_ids_list:
                item_data = df[df['Item ID'] == every_item_id]
                sanitized_item_id = re.sub(r'[^\w\-_. ]', '', str(every_item_id))
                filename = os.path.join(folder_path, f'{sanitized_item_id}.csv')
                item_data.to_csv(filename, index=False)
            print("Unique Battery Id Data files created successfully...")
        except FileNotFoundError as e:
            print("Error in unique id data file creation (Battery) : ",e)

    def unique_dealer_finder_battery(self, directory):
        try:
            df = pd.read_csv(directory)
            unique_dealers_list = df['Dealer'].unique()
            folder_path = 'application/datafiles/battery_data_files/unique_battery_dealer_data_files'

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            for every_dealer in unique_dealers_list:
                item_data = df[df['Dealer'] == every_dealer]
                sanitized_dealer = re.sub(r'[^\w\-_. ]', '', str(every_dealer))
                filename = os.path.join(folder_path, f'{sanitized_dealer}.csv')
                item_data.to_csv(filename, index=False)
            print("Unique Battery Dealer Data files created successfully...")
        except FileNotFoundError as e:
            print("Error in unique dealer data file creation (Battery) : ",e)

    def unique_year_finder_battery(self, directory):
        try:
            df = pd.read_csv(directory)
            unique_years_list = df['Year'].unique()
            folder_path = 'application/datafiles/battery_data_files/unique_battery_year_data_files'

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            for every_year in unique_years_list:
                item_data = df[df['Year'] == every_year]
                sanitized_year = re.sub(r'[^\w\-_. ]', '', str(every_year))
                filename = os.path.join(folder_path, f'{sanitized_year}.csv')
                item_data.to_csv(filename, index=False)
            print("Unique Battery Year Data files created successfully...")
        except FileNotFoundError as e:
            print("Error in unique year data file creation (Battery) : ",e)
