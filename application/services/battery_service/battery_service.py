from application.repositories.battery_repository.battery_repository import BatteryRepository

battery_repository = BatteryRepository()

class BatteryService:
    def pre_processer_battery(self, directory):
        battery_repository.pre_processor_battery(directory)

    def unique_id_finder_battery(self, directory):
        battery_repository.unique_id_finder_battery(directory)

    def unique_dealer_finder_battery(self, directory):
        battery_repository.unique_dealer_finder_battery(directory)

    def unique_year_finder_battery(self, directory):
        battery_repository.unique_year_finder_battery(directory)



