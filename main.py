import requests
api_key = '693e0077f4d41e43381f2bc9f0a2eaba'
city= input("Enter the city : ")
url = "https://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city
Response = requests.get(url).json()
print(Response)

Temp =  Response['main']['temp']
Climate = Response['weather'][0]['main']
print("/////////////////////////////////////////////////////////////////////////")
print("Temperature: ",Temp)
weather_icons = {'01d':'☀️','02d':'⛅','03d':'☁️','04d':'☁️','09d':'🌧️','10d':'🌦️','11d':'🌩️','13d':'❄️','50d':'🌫️',
                 '01n':'☀️','02n':'⛅','03n':'☁️','04n':'☁️','09n':'🌧️','10n':'🌦️','11n':'🌩️','13n':'❄️','50n':'🌫️'}
print("Climate: ",Climate, weather_icons.get(Response['weather'][0]['icon']))

print(list(weather_icons))