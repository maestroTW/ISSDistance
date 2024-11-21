from haversine import haversine
import ISS, User

Distance = round(haversine(ISS.Cord, User.Cord), 2), "km"

Mid0 = ((User.Cord[0]-ISS.Cord[0]) / 2)
Mid1 = ((User.Cord[1]-ISS.Cord[1]) / 2)
MidDistance = [ISS.Cord[0] + Mid0, ISS.Cord[1] + Mid1]
