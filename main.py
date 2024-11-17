from geopy.geocoders import Nominatim
import requests
from haversine import haversine

location = Nominatim(user_agent="GetLoc")
getLocation = location.geocode(input("Your address: "))
MyCord = float(getLocation.latitude), float(getLocation.longitude)

url = 'http://api.open-notify.org/iss-now.json'
json_data = requests.get(url).json()
ISSСord = float(json_data['iss_position']['latitude']), float(json_data['iss_position']['longitude'])

print("МКС: ",ISSСord, "Ты: ", MyCord)
print(haversine(ISSСord, MyCord), "km")
