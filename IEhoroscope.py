import bs4                             # using beautiful soup for web scraping
import requests

from gtts import gTTS                  # using Google Text-to-Speech engine for conversion
import os
import subprocess

print("Googling...")

# res = requests.get("https://indianexpress.com/article/horoscope/horoscope-today-august-24-2019-aquarius-taurus-aries-sagittarius-capricorn-cancer-check-astrology-prediction-5911008/")
# res = requests.get("https://indianexpress.com/article/horoscope/horoscope-today-august-23-2019-sagittarius-taurus-aries-sagittarius-pisces-cancer-leo-check-astrology-prediction-5910966/")
res = requests.get("https://indianexpress.com/article/horoscope/horoscope-today-september-7-2019-libra-leo-scorpio-virgo-pisces-taurus-aries-check-astrology-prediction-5950587/")


soup = bs4.BeautifulSoup(res.text, 'lxml')

soup.select('article')

with open ("IEhoroscope.txt", 'w') as f:
    for i in soup.select('article'):
        f.write(i.text)

print("Getting your horoscope!")

with open ("myIEhoroscope.txt", 'w') as f:
    x = 'tail IEhoroscope.txt | grep -i -A1 "Pisces" '
    ps = subprocess.run(x, shell=True, stdout=subprocess.PIPE, text=True)
    print(ps.stdout)
    f.write(ps.stdout)

print("Preparing the speech response!")

with open ("myIEhoroscope.txt", 'r') as f:
    mytext = f.read()
    language = 'en'
    obj = gTTS(text=mytext, lang = language, slow=False)
    obj.save('IEhoroscope.mp3')

print("Speaking...")

os.system("mpg123 IEhoroscope.mp3 > /dev/null 2>&1")                                # you may comment this is it craetes error (better to comment if you're on windows system)
# os.system("shred -u IEhoroscope.txt myIEhoroscope.txt IEhoroscope.mp3")           # uncomment this this you work on a linux system

os.remove("IEhoroscope.txt")                                                       # comment these three if you've un commented the above command
os.remove("myIEhoroscope.txt")
os.remove("IEhoroscope.mp3")


print("Thankyou for using the service!")











