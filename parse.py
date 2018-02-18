from lxml import html
import requests


def get_all_hackathons():
    page = requests.get('https://mlh.io/seasons/na-2018/events')
    tree = html.fromstring(page.content)
    names = tree.xpath('//h3[@itemprop="name"]/text()')
    location = tree.xpath('//span[@itemprop="addressLocality"]/text() | // span[ @ itemprop = "addressRegion"] / text()')

    print names
    print location

get_all_hackathons()
