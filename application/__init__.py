from flask import Flask, session

from application.securefiles.secretkey import SESSION_ENABLE_KEY
from application.services.battery_service.battery_service import BatteryService

app = Flask(__name__)


from application import routes



