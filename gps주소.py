from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geo_app")
location = geolocator.reverse(" , ") # 위도, 경도 입력 

print(location.address)