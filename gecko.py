# -*- coding: future_fstrings -*-
import telepo,requests,time,os
from bs4 import BeautifulSoup

userid = "" #your telegram channel ID 
token = "" # API token from @botfather 

bot=telepot.Bot(token)
default="https://www.ccmalaysia.com/wp-content/uploads/2018/04/DQmWJDVhm1dgKZHbk4K1Es6MzhF1tDHvgotxb9Fbkv3Y8tf-768x385.png" # Any default image link    

data = []

while True: # Main Part
	res = requests.get('https://www.coingecko.com/en/news')
	soup = BeautifulSoup(res.content, 'lxml')
	posts = soup.find_all('div', class_ = "col-lg-4 featured")
	for post in posts [:1] :
		title = post.find('h3').text  
		url = post.find('a')['href']
		header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'https://www.google.com/'
		}
		subres = requests.get(url,headers=header)
		subl = BeautifulSoup(subres.content,'lxml')
		try:
			img = subl.find("meta",  property="og:image").get('content')
		except:
			img = default
		try:
			subx = subl.find('meta', {'name':'description'}).get('content')
		except: 
			subx = "\n"
		sub = subx.replace('&rsquo;','')
		text = f"🔥 <b>{title}</b> !\n\n<i>{sub}\n\n</i><b>📰 Source :</b> {url}"
		if title in data:
			pass
		else:
			data.append(title)
			try: # To ignore the Bad Request Error so the bot keeps running..
			bot.sendPhoto(user,img,caption=text ,parse_mode='HTML')
			except:
				pass
			if len(data) == 12000: # Prevent data from gettig very big ;)
				data = data[:1000]