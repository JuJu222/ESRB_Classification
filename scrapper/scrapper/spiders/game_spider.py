import scrapy
import json


class GameSpider(scrapy.Spider):
    name = 'games'
    start_urls = [
        'https://www.esrb.org/search/?searchKeyword=&platform=Nintendo%20Switch%2CPlayStation%205%2CPlayStation%204%2CXbox%20Series%2CXbox%20One%2CPC&rating=E%2CE10%2B%2CT%2CM%2CAO&descriptor=All%20Content&pg=1&searchType=All&ielement%5B%5D=all'
    ]
    headers = {
        ':authority': 'www.esrb.org',
        ':method': 'POST',
        ':path': '/wp-admin/admin-ajax.php',
        ':scheme': 'https',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,id;q=0.8',
        'referer': 'https://www.esrb.org/search/?searchKeyword=&platform=Nintendo%20Switch,PlayStation%205,PlayStation%204,Xbox%20Series,Xbox%20One,PC&rating=E,E10+,T,M,AO&descriptor=All%20Content&pg=1&searchType=All&ielement[]=all',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    # form_data = {
    #     'action': 'search_rating',
    #     'searchKeyword': '',
    #     'searchType': 'All',
    #     'pg': 1,
    #     'platform'
    # }

    def parse(self, response, **kwargs):
        url = 'https://www.esrb.org/wp-admin/admin-ajax.php'
        request = scrapy.Request(url, method='POST', callback=self.parse_api, headers=self.headers)
        yield request

    def parse_api(self, response):
        raw_data = response.body
        data = json.loads(raw_data)
        for game in data:
            yield {'game': game}
