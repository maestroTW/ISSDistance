import requests

url = 'http://api.open-notify.org/iss-now.json'
json_data = requests.get(url).json()
Сord = float(json_data['iss_position']['latitude']), float(json_data['iss_position']['longitude'])