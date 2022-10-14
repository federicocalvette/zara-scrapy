from urllib import response
from bs4 import BeautifulSoup
import requests

def make_request():
    headers = {
        'authority': 'www.zara.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'es-419,es;q=0.9',
        'cache-control': 'max-age=0',
        'if-none-match': 'W/"dc5b3-ifjum79vKCRO9uBk1rkK1HIzBgw"',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }

    response = requests.get('https://www.zara.com/uy/es/join-life-man-shirts-l3030.html', headers=headers)

    return response

def get_start_urls():

    response = make_request()

    soup = BeautifulSoup(response.content, 'html.parser')

    urls_href_camisas = []

    for a_camisa in soup.find_all('a', 'product-link _item product-grid-product-info__name link'):
            href = a_camisa.get('href')
            urls_href_camisas.append(href)

    return urls_href_camisas



