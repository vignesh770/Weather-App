from django.shortcuts import render

# Create your views here.

import urllib.request
import json


def index(request):
    if request.method == 'post':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&apiid=8881e2ad52d370a0459c5a37bcf51b8a').read()
        list_of_data = json.loads(source)

        data = {
            "coordinate":str(list_of_data['coord']['lon'] + ','+ str(list_of_data['coord']['lat']),),
            "temp":str(list_of_data['main']['temp'])+'C',
            "country_code":str(list_of_data['sys']['country']),
            "humidity":str(list_of_data['main']['humidity']),
            "pressure":str(list_of_data['main']['pressure']),
            "description":str(list_of_data['weather'][0]['description']),
            "main":str(list_of_data['weather'][0]['main']),
            "icon":list_of_data['weather'][0]['icon']
        }
        print(data)
    else:
        data = {}

    return render(request,"main/index.html",data)