#!/usr/bin/env python3
import json
import requests
from requests.cookies import cookiejar_from_dict
from bs4 import BeautifulSoup as BSoup
from sys import stderr


EGGLANDS_BEST_URL = "https://www.foodcity.com/product/823/0071514150349"


with requests.Session() as session:
    # load cookies
    with open('cookies.json', 'r') as fp:
        cookie_dict = json.load(fp)

    session.cookies = cookiejar_from_dict(cookie_dict)

    r = session.get(EGGLANDS_BEST_URL) # noqa
    # if 'set-cookie' in r.headers:
    #     print("Server sends set-cookie", file=stderr)

    soup = BSoup(r.text, "html.parser")
    print(soup.find('span', class_="item-detail__price").string.strip())

    # save cookies
    with open('cookies.json', 'w') as fp:
        json.dump(session.cookies.get_dict(), fp, sort_keys=True, indent=4)
