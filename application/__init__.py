from flask import Flask
from application.services.battery_service.battery_service import BatteryService

app = Flask(__name__)


from application import routes



