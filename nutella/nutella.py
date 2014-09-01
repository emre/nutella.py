# -*- coding: utf-8 -*-

import requests
import re

NUTELLAS = {
    " 39 GR": "http://www.sanalmarket.com.tr/kweb/prview/47371036-30489-nutella-go-39-g/",
    "400 GR": "http://www.sanalmarket.com.tr/kweb/prview/5231368-30489-nutella-400-gr/",
    "750 GR": "http://www.sanalmarket.com.tr/kweb/prview/17671377-30489-nutella-750-gr/",
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
}


def main():
    for nutella, url in NUTELLAS.items():
        price = re.search('<span itemprop="price">(.*?)</span>', requests.get(url, headers=headers).content)
        if price:
            print "  \xF0\x9F\x8D\xAB  {}: {} TL.".format(nutella, price.group(1))


if __name__ == '__main__':
    main()
