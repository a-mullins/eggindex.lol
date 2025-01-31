#!/usr/bin/env python3
import browser_cookie3
import json
import requests
from bs4 import BeautifulSoup as BSoup

EGGLANDS_BEST_URL = "https://www.foodcity.com/product/823/0071514150349"

with requests.Session() as session:
    jar = requests.cookies.RequestsCookieJar()
    jar.update(browser_cookie3.firefox())
    session.cookies = jar

    r = session.get(EGGLANDS_BEST_URL) # noqa

    with open('cookies.json', 'w') as fp:
        d = dict((s.strip().split('=')
                  for s
                  in r.request.headers['Cookie'].split(';')))
        json.dump(d, fp, sort_keys=True, indent=4)

    soup = BSoup(r.text, "html.parser")
    print(soup.find('span', class_="item-detail__price").string.strip())
