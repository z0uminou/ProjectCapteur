from celery import shared_task
from .models import TemperatureReading
from .TensorManagement import TemperatureSensorManager


@shared_task
def record_temperature(hive_id):
    sensor_manager = TemperatureSensorManager()
    temperatures = sensor_manager.get_temperatures()  # Obtenir les températures
    for sensor_name, temperature in temperatures:
        TemperatureReading.objects.create(hive_id=hive_id, temperature=temperature)