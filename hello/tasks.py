
from web_project.settings import HUEY
#from huey import crontab
from .models import TemperatureReading
from .TensorManagement import TemperatureSensorManager


@HUEY.periodic_task(crontab(minute='0', hour='3'))
def record_temperature(hive_id):
    sensor_manager = TemperatureSensorManager()
    temperatures = sensor_manager.get_temperatures()  # Obtenir les températures
    for sensor_name, temperature in temperatures:
        TemperatureReading.objects.create(hive_id=hive_id, id_capteur= sensor_name, temperature=temperature)