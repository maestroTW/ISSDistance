from geopy.geocoders import Nominatim

location = Nominatim(user_agent="GetLoc")
getLocation = location.geocode(input("Your address: "))
Cord = float(getLocation.latitude), float(getLocation.longitude)