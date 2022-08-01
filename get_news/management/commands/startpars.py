from django.core.management.base import BaseCommand, CommandError

import requests
from bs4 import BeautifulSoup
import urllib3

from ...models import News



class Command(BaseCommand):
    urllib3.disable_warnings()

    def handle(self, *args, **options):
        url = 'https://saratov.gov.ru/news/'
        curl = 'https://saratov.gov.ru'
        r = requests.get(url, verify=False)
        soup = BeautifulSoup(r.text, 'lxml')
        url_title_list = soup.find_all('a', class_="title with-preview")

        for text in url_title_list:
            url_new = curl + text.get('href')
            new_text = requests.get(url_new, verify=False)
            soup_cont = BeautifulSoup(new_text.text, 'lxml')
            cont = soup_cont.find_all('div', class_="text-full")
            content = "".join([t.text for t in cont])
            News.objects.create(title=text.text, url=url_new, content=content)


