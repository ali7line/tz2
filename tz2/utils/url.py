from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


def wait_for_table(browser):
    for i in range(20):
        if browser.title == 'Search torrent':
            return True
        else:
            sleep(0.5)
    raise "Page did not load"



def get_url(url, browser=None):
    if not browser:
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.socks", 'localhost')
        profile.set_preference("network.proxy.socks_port", 8082)
        profile.set_preference("network.proxy.socks_remote_dns", True)
        browser = webdriver.Firefox(firefox_profile=profile)
        browser.get(url)
        wait_for_table(browser)

    html_text = browser.page_source
    return html_text, browser


def parse_search(html_text):
    bsObj = BeautifulSoup(html_text, 'html.parser')
    results = bsObj.find_all('div', class_='results')[0]
    total_number = results.find_all('h2')[0].text
    rows = results.find_all('dl')
    table = []
    for i, r in enumerate(rows):
        name = r.a.text
        link = 'https://torrentz2.eu' + r.a['href']
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

    result = (hashinfo, trackers,)
    return result


if __name__ == '__main__':
    with open('/tmp/link.html', 'r') as f:
        html_text = f.read()

    result = parse_link(html_text)
    print(result)
