import json
import requests
r=requests.get('https://www.metaweather.com/api/location/2306179/2018/7/18')
r.encoding='utf-8'
# print(r.text)

data=json.loads(r.text)
print("creat weather time\t\t","weather state")
for i in range(0,len(data)):
    print(data[i]['created']+"\t"+data[i]['weather_state_name'])