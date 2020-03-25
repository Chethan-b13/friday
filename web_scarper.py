import pandas as pd
from bs4 import BeautifulSoup
import requests
from Text_to_speech import speak


def get_news():
    page = requests.get('https://www.indiatoday.in/india?page=2')
    news_soup = BeautifulSoup(page.content, 'html.parser')
    headings = news_soup.find_all(class_='detail')
    titles = [heading.find("a").get_text() for heading in headings]
    news_df = pd.DataFrame(
        {
            'Top news': titles
        }
    )
    news_df.to_csv(r'news.txt', header=None, index=None, sep=' ', mode='w')
    with open('news.txt', 'r') as f:
        Text_o = str(f.read().replace('\n', ','))
        speak(Text_o)


# noinspection PyArgumentList
def weather_report():
    weather_page = requests.get("https://www.bbc.com/weather/1277333")
    soup = BeautifulSoup(weather_page.content, 'html.parser')
    block = soup.find(id='daylink-0')
    time = block.find('span').get_text()
    max_temp = block.find('span', {"class": "wr-value--temperature--c"}).get_text()
    disc = block.find('div', {
        "class": "wr-day__weather-type-description wr-js-day-content-weather-type-description "
                 "wr-day__content__weather-type-description--opaque"}).get_text()
    speak("{} it is {} celsius , {}".format(time, max_temp, disc))
