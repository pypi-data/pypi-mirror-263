import requests

class PyAD:
    def ip(self):
        response_ip = requests.get('https://api.ipify.org?format=json')
        public_ip = response_ip.json()['ip']
        return public_ip
    
    
    

class PyLO:
    def get_location(self, ip_address):
        response_geo = requests.get(f'http://ip-api.com/json/{ip_address}')
        geo_data = response_geo.json()
        if geo_data['status'] == 'success':
            return geo_data['lat'], geo_data['lon']
        else:
            return None, None

class PyCU:
    def get_country(self , ip_address):
        response_geo = requests.get(f'http://ip-api.com/json/{ip_address}')
        geo =response_geo.json()
        if geo['status'] == 'success':
            return geo['country'], geo['regionName']
        else:
            return None ,None


# ad = PyLO()

# ip_address = 'عنوان الip هنا'

# latitude, longitude = ad.get_location(ip_address)
# if latitude and longitude:
#     print(f"Latitude: {latitude}, Longitude: {longitude}")
# else:
#     print("عنوان IP غير صالح أو حدث خطأ في الاستعلام.")