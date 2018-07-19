import requests
import json
url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
response = requests.get(url)


with open('music_show.txt','w',encoding='utf-8') as f:
    text = json.loads(response.text)
    for i in text:
        f.write(i['title']+i['startDate']+ '~' +i['endDate']+'\n')
     
    pass