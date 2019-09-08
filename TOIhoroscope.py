import bs4                        # using beautiful soup for web scraping
import requests

from gtts import gTTS             # using Google Text-to-Speech engine for conversion
import os
import subprocess

print("Googling...")

# res = requests.get("https://timesofindia.indiatimes.com/astrology/horoscope/horoscope-today-august-24-2019-check-astrological-prediction-for-leo-virgo-libra-scorpio-and-other-signs/articleshow/70813500.cms")
# res = requests.get("https://timesofindia.indiatimes.com/astrology/horoscope/horoscope-today-august-25-2019-check-astrological-prediction-for-leo-virgo-libra-scorpio-and-other-signs/articleshow/70824506.cms")
res = requests.get("https://timesofindia.indiatimes.com/astrology/horoscope/horoscope-today-september-7-2019-check-astrological-prediction-for-aries-taurus-gemini-cancer-and-other-signs/articleshow/71019210.cms")


soup = bs4.BeautifulSoup(res.text, 'lxml')

# soup.select('.Normal')

with open ("TOIhoroscope.txt", 'w') as f:   
    for i in soup.select('.Normal'):
        f.write(i.text)

print("Getting your horoscope!")

with open ("myTOIhoroscope.txt", 'w') as f:
    x = 'grep -A1 "Pisces" TOIhoroscope.txt'
    ps = subprocess.run(x, shell=True, stdout=subprocess.PIPE, text=True)
    f.write(ps.stdout)

print("Preparing the speech response!")

with open ("myTOIhoroscope.txt", 'r') as f:
    mytext = f.read()
    language = 'en'
    obj = gTTS(text=mytext, lang = language, slow=False)
    obj.save('TOIhoroscope.mp3')

print("Speaking...")

os.system("mpg123 TOIhoroscope.mp3 > /dev/null 2>&1")                                # you may comment this is it craetes error (better to comment if you're on windows system)
# os.system("shred -u TOIhoroscope.txt myTOIhoroscope.txt TOIhoroscope.mp3")         # uncomment this this you work on a linux system

os.remove("TOIhoroscope.txt")                                                        # comment these three if you've un commented the above command
os.remove("myTOIhoroscope.txt")
os.remove("TOIhoroscope.mp3")

print("Thankyou for using the service!")











