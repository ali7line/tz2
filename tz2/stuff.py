from selenium import webdriver
from time import sleep

ROOT_URL = 'https://torrentz2.eu'
DEFAULT_URL = 'https://torrentz2.eu/search'
MAX_WAIT = 20


class Result():
    def __init__(self, **kwargs):
	#name tags link verified (bool) age size seed leech trackers hashinfo magnet
        self.__dict__.update(**kwargs)

    def parse_search_page(driver):
        div_results = driver.browser.find_element_by_xpath("//div[contains(@class, 'results')]")
        found_result = div_results.find_element_by_tag_name('h2').text      # '61,106,814 Torrents'
        results = []
        for row in div_results.find_elements_by_tag_name('dl'):
            # information in dt portion
            self.name, self.tags = row.find_element_by_tag_name('dt').text.split('»')
            self.link = row.find_element_by_tag_name('a').get_attribute('href')
            # information in dd portion
            detail = row.find_element_by_tag_name('dd')
            self.verified = detail.find_elements_by_tag_name('span')[0].text
            self.age = detail.find_elements_by_tag_name('span')[1].text
            self.size = detail.find_elements_by_tag_name('span')[2].text
            self.seed = detail.find_elements_by_tag_name('span')[3].text
            self.leech = detail.find_elements_by_tag_name('span')[4].text

    def parse_torrent_page(driver):
        trackers = []
        trackers_info = driver.browser.find_element_by_xpath("//div[contains(@class, 'trackers')]")
        for tracker in trackers_info.find_elements_by_tag_name('dt'):
            trackers.append(tracker.text)

        self.hash = trackers_info.find_element_by_tag_name('h2').text.split(' ')[-1]
        self.magnet = magnetize(hash, trackers)


class Browser():
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


#if __name__ == '__main__':
#    d = {'name': 'Manifest.S01E10.HDTV.x264-KILLERS[rarbg] ', 'tags': ' video tv', 'link': 'https://torrentz2.eu/09c8d17694c1a4141cfcdb65d266c6b88e009b33', 'verified': '✓', 'age': '2 days', 'size': '248 MB', 'seed': '371', 'leech': '38'}
#    r = Result(**d)
#    print(r.__dict__)
