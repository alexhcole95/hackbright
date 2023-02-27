import bs4
import requests


def get_word_from_webpage(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#dictionary-entry-1 > div.row.entry-header > div > div.entry-header-content.d-flex.flex-wrap.align-items-baseline.flex-row.mb-0 > h1')
    return elems[0].text.strip()


price = get_word_from_webpage('https://www.merriam-webster.com/dictionary/test')
print('The word is ' + price)
