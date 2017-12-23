from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import request
import time

rank = 1
f = open('DouBan_Top250.txt', 'w') #write down list to this file
for i in range(0, 226,25):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(i) #This url is for DOUBAN website top 250 movies rank
    req = request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36') # cpoy the head information, make Web Crawler
    html_url = request.urlopen(req)
    html_text = html_url.read().decode('utf-8') # Decode the file from binary information into normal string
    soup = BeautifulSoup(html_text, 'html.parser')# loading hteml source code into "beautiful soup"
    index_div = soup.find('div', class_='grid-16-8 clearfix')  #find all div with class
    movie_title = index_div.find_all('span', class_='title')
    movie_url = index_div.find_all('a')
    for (str,url) in zip(movie_title, movie_url):
        if str.contents[0][0] != '\xa0':
            print (rank,':',str.contents[0])
            line = 'Rank：{}-名字：{}\n'.format(rank,str.contents[0])
            rank = rank + 1
            f.write(line)
            print (url['href'])
            line = 'Url：{}\n'.format(url['href'])
            f.write(line)
        else:
            continue
    time.sleep(5)

f.close()
