from bs4 import BeautifulSoup
import requests
def get_featured(date):
    Article_code =  requests.get('https://www.britannica.com/on-this-day/{0}'.format(date)).text
    soup = BeautifulSoup(Article_code, 'lxml')
    event = soup.find('div', class_ = 'featured-event-card card')
    text_field = event.find('div', class_ = 'card-body')
    all_divs = text_field.find_all('div')
    s = ""
    for i in all_divs:
        if i == all_divs[-1]:
            s = s + 'Source: {0}\n\n'.format(i.text)
        else:
            s = s + '{0}\n\n'.format(i.text)
    return s





