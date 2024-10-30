from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .TensorManagement import TemperatureSensorManager
import time  # pour la simulation du délai de mesure



# Create your views here.

def home(request):
    return HttpResponse("Hellow, Django !")

@login_required
def dashboard(request):
    # Récupérer les relevés de température pour l'utilisateur
    readings = TemperatureReading.objects.filter(hive_id="ID de la ruche")
    return render(request, 'dashboard.html', {'readings': readings})


#print("Noms des capteurs:", sensor_names)


def get_sensor_data():
    # Remplacez par votre code de récupération des données 1-wire
    return TemperatureSensorManager(get_temperatures)  # Exemple : température en °C

def record_temperature(request):
    if request.user.is_authenticated:
        hive_id = request.GET.get('hive_id')
        temperature = get_sensor_data()
        TemperatureReading.objects.create(hive_id=hive_id, temperature=temperature)
        return JsonResponse({'status': 'success', 'temperature': temperature})
    return JsonResponse({'status': 'error', 'message': 'User not authenticated'})