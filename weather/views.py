from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


def Home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Allahabad'

    # exception_occurred = False

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0c10f8d7d8d184c90547afec65619d62&units=metric'



    API_KEY =  'AIzaSyBsQfkLmrkcdQzP18mYNgVzihiiYduTuyc'

    SEARCH_ENGINE_ID = 'b0b6a2cdc7efb489d'
     
    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']



    try:
        exception_occurred = False
        data = requests.get(url).json()

        
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        context = {
        'city':city,
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'exception_occurred':exception_occurred,
        'image_url':image_url
        }

        return render(request, 'weather_app/index.html', context)

        
    except KeyError:
        exception_occurred = True
        messages.error(request,'Entered data is not available to API')


        city = 'Allahabad'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0c10f8d7d8d184c90547afec65619d62&units=metric'
        data = requests.get(url).json()

        
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        
        query = city + " 1920x1080"
        page = 1
        start = (page - 1) * 10 + 1
        searchType = 'image'
        city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

        data = requests.get(city_url).json()
        count = 1
        search_items = data.get("items")
        image_url = search_items[1]['link']

        context = {
        'city':city,
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'exception_occurred':exception_occurred,
        'image_url':image_url


        }

        return render(request,'weather_app/index.html' ,context)
    

    

    
