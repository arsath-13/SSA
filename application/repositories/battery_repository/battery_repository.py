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
            preprocess_message = "Battery Data file preprocessing is completed successfully..."
            print(preprocess_message)
            return preprocess_message
        except FileNotFoundError as e:
            preprocess_message = ("Error in Pre-processing (Battery) : ",e)
            print(preprocess_message)
            return preprocess_message

    def unique_id_finder_battery(self, directory):
        try:
            df = pd.read_csv(directory)
            unique_ids_list = df['Item ID'].unique()
            unique_names_list = df['Item name'].unique()
            sorted_unique_names_list = sorted(unique_names_list)
            folder_path = 'application/datafiles/battery_data_files/unique_battery_id_data_files'

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            for every_item_id in unique_ids_list:
                item_data = df[df['Item ID'] == every_item_id]
                sanitized_item_id = re.sub(r'[^\w\-_. ]', '', str(every_item_id))
                filename = os.path.join(folder_path, f'{sanitized_item_id}.csv')
                item_data.to_csv(filename, index=False)
            unique_id_creator_message = "Unique data files based on Item Id, are created successfully..."
            print(unique_id_creator_message)
            return unique_id_creator_message, sorted_unique_names_list

        except FileNotFoundError as e:
            unique_id_creator_message = ("Error in unique id data file creation (Battery) : ",e)
            print(unique_id_creator_message)
            return unique_id_creator_message

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
            unique_dealer_creator_message = "Unique data files based on dealers, are created successfully..."
            print(unique_dealer_creator_message)
            return unique_dealer_creator_message
        except FileNotFoundError as e:
            unique_dealer_creator_message = ("Error in unique dealer data file creation (Battery) : ",e)
            print(unique_dealer_creator_message)
            return unique_dealer_creator_message

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

            unique_year_creator_message = "Unique data files based on years, are created successfully..."
            print(unique_year_creator_message)
            return unique_year_creator_message
        except FileNotFoundError as e:
            unique_year_creator_message = ("Error in unique year data file creation (Battery) : ",e)
            print(unique_year_creator_message)
            return unique_year_creator_message
