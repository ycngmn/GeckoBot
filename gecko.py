import telepot,requests,time
from bs4 import BeautifulSoup

user = "@NewsGecko" #your telegram channel username
token = "" # API token from @botfather 

bot=telepot.Bot(token)
default="https://example.c/ex.png" # Any image link to use if no image found in post..   

data = []

while True: # Main Part Begins
	res = requests.get('https://www.coingecko.com/en/news')
	soup = BeautifulSoup(res.content, 'lxml')
	posts = soup.find_all('div', class_ = "col-lg-4 featured")
	for post in posts:
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
			subx = "( Unable to get the description)"
		sub = subx.replace('&rsquo;','')
		text = f"🔥 <b>{title}</b> !\n\n<i>{sub}\n\n</i><b>📰 Source :</b> {url}"
		if title.endswith('?'):
			text = f"🔥 <b>{title}</b> \n\n<i>{sub}\n\n</i><b>📰 Source :</b> {url}"

		if title in data:
			pass
		else:
			data.append(title)
			try: # Mostly Except bad requests error.. 
				bot.sendPhoto(user,img,caption=text ,parse_mode='HTML')
			except Exception as e:
				print(e)
		if len(data) > 20: # to keep data's data in limit XD
			data = data[-5:]