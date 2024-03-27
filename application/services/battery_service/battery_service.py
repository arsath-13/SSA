from application.repositories.battery_repository.battery_repository import BatteryRepository

battery_repository = BatteryRepository()

class BatteryService:
    # def validator(self, directory):
    #     validator_message = battery_repository.validator(directory)
    #     return validator_message

    def pre_processer_battery(self, directory):
        preprocess_message = battery_repository.pre_processor_battery(directory)
        return preprocess_message

    def unique_id_finder_battery(self, directory):
        unique_id_creator_message, unique_names_list = battery_repository.unique_id_finder_battery(directory)
        return unique_id_creator_message, unique_names_list
    def unique_dealer_finder_battery(self, directory):
        unique_dealer_creator_message = battery_repository.unique_dealer_finder_battery(directory)
        return unique_dealer_creator_message

    def unique_year_finder_battery(self, directory):
        unique_year_creator_message = battery_repository.unique_year_finder_battery(directory)
        return unique_year_creator_message



