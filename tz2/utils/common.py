from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

ROOT_URL = 'https://torrentz2.eu'
DEFAULT_URL = 'https://torrentz2.eu/search'
MAX_WAIT = 20

class TZ2():
    def wait_for(self, thing):
        # thing could be /seach_page/torrent page/tracker page
        pass

    def wait_for_table(self):
        for i in range(MAX_WAIT):
            if self.browser.title == 'Search torrent':
                return True
            else:
                sleep(1)
        raise "Page did not load"

    def __init__(self, proxy=True):
        if proxy:
            profile = webdriver.FirefoxProfile()
            profile.set_preference("network.proxy.type", 1)
            profile.set_preference("network.proxy.socks", 'localhost')
            profile.set_preference("network.proxy.socks_port", 8082)
            profile.set_preference("network.proxy.socks_remote_dns", True)
            self.browser = webdriver.Firefox(firefox_profile=profile)
        else:
            self.browser = webdriver.Firefox()

        self.browser.get(DEFAULT_URL)
        self.wait_for_table()

    def parse_search(self):
        bsObj = BeautifulSoup(self.browser.page_source, 'html.parser')
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


    def parse_link(self):
        bsObj = BeautifulSoup(self.browser.page_source, 'html.parser')
        trackers_table = bsObj.find_all('div', class_='trackers')[0]
        hashinfo = trackers_table.h2.text.split(' ')[-1]
        trackers = [t.text for t in trackers_table.find_all('dt')]

        result = (hashinfo, trackers,)
        return result


if __name__ == '__main__':
    page = TZ2()
