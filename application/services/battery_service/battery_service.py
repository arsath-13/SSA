from application.repositories.battery_repository.battery_repository import BatteryRepository

battery_repository = BatteryRepository()

class BatteryService:

    def pre_processer_battery(self, file):
        preprocess_message, df = battery_repository.pre_processor_battery(file)
        return preprocess_message, df

    def unique_id_finder_battery(self, file):
        unique_id_creator_message, unique_names_list, number_of_unique_ids = battery_repository.unique_id_finder_battery(file)
        return unique_id_creator_message, unique_names_list, number_of_unique_ids

    def unique_dealer_finder_battery(self, directory):
        unique_dealer_creator_message, number_of_unique_dealers = battery_repository.unique_dealer_finder_battery(directory)
        return unique_dealer_creator_message, number_of_unique_dealers

    def unique_year_finder_battery(self, directory):
        unique_year_creator_message, unique_years_list = battery_repository.unique_year_finder_battery(directory)
        return unique_year_creator_message, unique_years_list

    def add_data(self, data, csv_path):
        flag = battery_repository.add_data(data,csv_path)
        return flag



