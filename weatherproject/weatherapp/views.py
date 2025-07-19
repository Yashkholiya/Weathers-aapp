from django.shortcuts import render
import requests 

# Create your views here.
def home(request):
    data = None
    error = None 
    
    if request.method == "POST":
        city = request.POST.get('city')
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=48d9012d50eaeaa60960eaff6379797d&units=metric'
        
        response = requests.get(url)
        data = response.json()
        
        if data.get("cod") == 200:
            data = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"],
            }
        else:
            error = "Not Found"
        
    return render(request , "index.html", {
        "data":data,
        "error":error,
    })
            
        