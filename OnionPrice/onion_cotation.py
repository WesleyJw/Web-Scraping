# This get the link pages that store cotation onion links

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def html_parser(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print(e)
    else:
        if html is None:
            print("Page empty!")
            return None
        else:
            return BeautifulSoup(html, "html.parser")


def get_page_url(url):
    # Get the pages links
    bs = html_parser(url)
    current = bs.find('span', {'class': 'current'}).get_text()
    title = str(int(current) + 1)
    try:
        next_page = bs.find('a', {'title': title}).attrs['href']
    except AttributeError:
        next_page = ""
    return next_page


def get_url_cotation(url):
    # Get the cotations links
    bs = html_parser(url)
    content = bs.find_all(
        'h3', {'class': 'entry-title td-module-title'})
    url_cotations = [url.find('a', href=True)['href']
                     for url in content]
    return url_cotations


def get_cotation(url):
    bs = html_parser(url)
    try:
        content = bs.find('div', {'class': 'td-post-content'}).find_all('p')[2]
        print(content)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    url = "https://www.didigalvao.com.br/page/1/?s=cota%C3%A7%C3%A3o+cebola"
    while url:
        print(url)
        cotations_links = get_url_cotation(url)
        for link in cotations_links:
            get_cotation(link)
        url = get_page_url(url)
        break
