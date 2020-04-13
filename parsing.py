import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from time import gmtime, strftime

#
url = 'https://www.google.com/search?newwindow=1&sxsrf=ALeKk03sYtT2MsOwb2m0Oajg0q_YOmpAhg%3A1586776367705&ei=L0mUXrbBKsnMrgSXy4igAQ&q=%D0%B3%D1%80%D0%B8%D0%BA%D0%BE%D1%81%D0%BB%D0%B0%D1%82%D0%BA%D0%B8%D1%83%D1%81&oq=%D0%B3%D1%80%D0%B8%D0%BA%D0%BE%D1%81%D0%BB%D0%B0%D1%82%D0%BA%D0%B8%D1%83%D1%81&gs_lcp=CgZwc3ktYWIQDFAAWABg1QRoAHAAeACAAQCIAQCSAQCYAQCqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwj2lPDNouXoAhVJposKHZclAhQQ4dUDCAw'


def get_text(soup,atr1,atr2):
    get = soup.findAll(attrs={atr1 : atr2})
    part_all = list()
    for i in range(len(get)):
        part = get[i].get_text()
        part = part.replace('\xa0',' ')
        part_all.append(part)

    return part_all


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:62.0) Gecko/20100101 Firefox/62.0'}
# par = {'page': u}
for i in range(300):
    r2 = requests.get(url, headers=headers)
    soup = BeautifulSoup(r2.text, 'html.parser')
    get = soup.find("div", {"id": "search"})


    urls = get_text(soup,'class','TbwUpd NJjxre')
    title = get_text(soup,'class','r')
    text = get_text(soup,'class','s')

    df = pd.DataFrame([urls, title, text]).T
    timeNow = strftime("%Y-%m-%d %H:%M:", gmtime())
    df['time'] = timeNow
    json_name = 'google_' + timeNow + '.csv'
    df.to_csv(json_name)

    print(i, timeNow)
    time.sleep(60*60*6)
