import requests
from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=<openweathermap-key>'
    print "Index page is called"
    form = CityForm()
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        req = requests.get(url.format(city))
        if(req.status_code != 404):            
#            r = requests.get(url.format(city)).json()
            r = req.json()
            city_weather = {
                'city' : city.name,
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
            }
            weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/weather.html', context)

@require_POST
def addCity(request):
    print ("Add City called")
    form = CityForm(request.POST)
    if form.is_valid():
        city = request.POST['name']
        print (city)
        city_found = False
        existing_cities = City.objects.all()
        print existing_cities
        for existing_city in existing_cities:
            if(city == existing_city.name):
                city_found = True
                print ("Duplicate City found") 
                break

        if(city_found == False):
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4da85e50a9e8c8b0e38766bcdb4de4da'
            r = requests.get(url.format(city))
            if(r.status_code == 404):
                website_link = "<a href=\"https://openweathermap.org/\">Openweathemap</a>" 
                wiki_link = "<a href=\"https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/country:_A-B\">Wiki</a>"
                cities_link = "<a href=\"http://bulk.openweathermap.org/sample/city.list.json.gz\">Cities</a>"
                error_str = "<h1><b>" + "\"" + city + "\" "+ "</b></h1>"
                error_str += """<h3>This City Name is not supported curently. The info about the 
                                Cities are retreived from """+ website_link +""" Website.<br/><br/>
                                The Cities supported are the usual standard names. <br/><br/>
                                For more info, Please refer to the """ + wiki_link + """ Page or the 
                                Official City names list provided by Openweathermap """ +cities_link+""" 
                                (File with Cities details will be downloaded).</h3>"""
                return HttpResponse(error_str)
            form.save()

    return redirect('index')
    
@require_POST
def delCity(request):
    print ("Del City called")
    form = CityForm(request.POST)
    if form.is_valid():
        city = request.POST['name']
        print (city)
        city_found = False
        existing_cities = City.objects.all()
        print existing_cities
        for existing_city in existing_cities:
            if(city == existing_city.name):
                city_found = True
                print ("Found the city in DB")
                break
        if(city_found == True):
            City.objects.get(name=city).delete()

    return redirect('index')
    
