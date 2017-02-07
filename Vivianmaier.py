__author__ = 'Chendi'
#下载http://www.vivianmaier.com/薇薇安迈尔的所公布的照片。
import requests
import urllib
from bs4 import BeautifulSoup
import re
#需要修改最后的url地址，依次为street-1/2/3/4/5，color-1/self-portraits/
#self-portraits-color。在使用爬虫前请访问http://www.vivianmaier.com/
res=requests.get('http://www.vivianmaier.com/gallery/street-1/')
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
count = 0
for url in soup.select('.rsImg'):
    if 'src' in url.attrs:
        count  = count + 1
        srcs = url.attrs['src']
        urllib.request.urlretrieve(srcs, 'D:\Vivianmaier\%d.jpg' % count)
print（“任务完成”）
