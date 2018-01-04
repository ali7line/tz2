from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def get_url(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req)
    html_text = html.read()
    return html_text


def parse_search(html_text):
    bsObj = BeautifulSoup(html_text, 'html.parser')
    results = bsObj.find_all('div', class_='results')[0]
    total_number = results.find_all('h2')[0].text
    rows = results.find_all('dl')
    table = []
    for i, r in enumerate(rows):
        name = r.a.text
        link = 'https//torrentz2.eu' + r.a['href']
        category = r.a.next_sibling
        # category = 'music'
        verfied, age, size, peers, leech = list(map(lambda x: x.text, r.find_all('span')))
        if verfied:
            verfied = 'Y'
        else:
            verfied = ' '

        table.append((i, name, category, verfied, age, size, peers, leech, link))
        # print('[{0}]: {1}'.format(i, name))

    return total_number, table


def parse_link(html_text):
    bsObj = BeautifulSoup(html_text, 'html.parser')
    trackers_table = bsObj.find_all('div', class_='trackers')[0]
    hashinfo = trackers_table.h2.text.split(' ')[-1]
    trackers = [t.text for t in trackers_table.find_all('dt')]

    result = (hashinfo, trackers)
    return result


if __name__ == '__main__':
    with open('/tmp/link.html', 'r') as f:
        html_text = f.read()

    result = parse_link(html_text)
    print(result)
