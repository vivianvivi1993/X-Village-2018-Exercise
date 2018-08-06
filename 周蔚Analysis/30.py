# data visualization

# 關於API獲得json檔案的資料
# 選擇豆瓣圖書

import json
import pandas as pd
import requests
import matplotlib.pyplot as plt
plt.rcdefaults()
from requests_html import HTMLSession
import re


url = 'https://api.douban.com/v2/book/4238362'
r = requests.get(url)
r.encoding = "utf-8"
r=r.json()
count=[]
name=[]
for i in r['tags']:
    count.append(i['count'])
    name.append(i['name'])
colors=['b','r','g','y','k','#9999ff','#ff9999','#7777aa']
plt.axes(aspect = 'equal')
plt.xlim(0,4)
plt.ylim(0,4)
plt.rcParams['font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus'] = False
plt.pie(x = count,labels = name,colors=colors,autopct = '%.1f%%',pctdistance = 0.8,radius=1.5,counterclock = False,
        center = (1.8,1.8),frame = 2)
plt.xticks(())
plt.yticks(())
plt.title('《送你一顆子彈》標籤分析')
plt.show()

# ==================================================
session = HTMLSession()
response = session.get('https://book.douban.com/')
element_rating = response.html.find('p.entry-star-small .average-rating')
element_bookname = response.html.find('li div.info h4.title a')
element_ratinglist=[]
element_booknamelist=[]
for i in element_rating:
    element_ratinglist.append(i.text)
list_to_float = list(map(lambda x:float(x), element_ratinglist))
for j in element_bookname:
    element_booknamelist.append(j.text)
# print(list_to_float,element_booknamelist)
plt.ylabel(u'熱門圖書名稱')
plt.xlabel(u'熱門圖書評分')
plt.title(u'最受關注圖書榜評分數據')
plt.rcParams['font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus'] = False
plt.barh(range(len(element_booknamelist)),list_to_float,fc='b',align = 'center',alpha = 0.41,left = 0,)
plt.yticks(range(len(element_booknamelist)),element_booknamelist)
series_1 =  pd.Series(list_to_float,index=element_booknamelist)
print(series_1)
plt.show()

# ======================
session = HTMLSession()
response = session.get('https://book.douban.com/tag/?view=type&icn=index-sorttags-all')
review_num = response.html.find('div#content td')
a = []
b = []
c = []
d = []
for i in review_num:
    a.append(re.findall(r'\d+',i.text))
    c.append(i.text)
for j in a:
    for ii in j:
        b.append(int(ii))

plt.figure(figsize=(160,200))
plt.xlim((0,10000000))
plt.ylim((0,150))
plt.grid(True, linestyle = "-", color = "grey", linewidth = "0.5",alpha = 0.3)
plt.rcParams['font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus'] = False
plt.barh(range(len(c)),b,fc='blue',align = 'center',alpha = 0.6,left = 0)
plt.yticks(range(len(c)),c)
plt.show()


