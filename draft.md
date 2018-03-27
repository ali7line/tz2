Result()
	# these come from result page
	tags
	name
	link
	verified (bool)
	age
	size
	seed
	leech

	# these come from the Result.link page
	trackers
	hashinfo

	# created using utils
	magnet


Browser()
	just holds the session

# searched page (lynda)





#parse_search_page(page)
	div_results = page.browser.find_element_by_xpath("//div[contains(@class, 'results')]")
	found_result = div_results.find_element_by_tag_name('h2').text 			# '61,106,814 Torrents'
	for row in div_results.find_elements_by_tag_name('dl'):
		name, tags = row.find_element_by_tag_name('dt').text..split('»')
		link = row.find_element_by_tag_name('a').get_attribute('href')
		detail = row.find_element_by_tag_name('dd')
		verified = detail.find_elements_by_tag_name('span')[0].text
		age = detail.find_elements_by_tag_name('span')[1].text
		size = detail.find_elements_by_tag_name('span')[2].text
		seed = detail.find_elements_by_tag_name('span')[3].text
		leech = detail.find_elements_by_tag_name('span')[4].text
	keys = ('name', 'tags', 'link', 'verified', 'age', 'size', 'seed', 'leech')
	values = (name, tags, link, verified, age, size, seed, leech)
	result = dict(zip(keys, values))
	return result 


parse_torrent_page(page)
	trackers = []
	trackers_info = page.browser.find_element_by_xpath("//div[contains(@class, 'trackers')]")
	for tracker in trackers_info.find_elements_by_tag_name('dt'):
	     trackers.append(tracker.text)

	hash = trackers_info.find_element_by_tag_name('h2').text.split(' ')[-1]
	magnet = magnetize(hash, trackers)

	return (trackers, hash, magnet)
