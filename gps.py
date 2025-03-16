import geocoder

# 현재 ip 기반으로 위치 가져오기
location = geocoder.ip('me')

print(f"위도: {location.lat}, 경도: {location.lng}")
print(f"대략적인 위치 : {location.city}, {location.country}")