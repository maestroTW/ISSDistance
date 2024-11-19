from haversine import haversine
import ISS, User

print("ISS:",ISS.Сord, "You:", User.Cord)
print("Distance:", round(haversine(ISS.Сord, User.Cord), 2), "km")
