from bs4 import BeautifulSoup


def parse_search(html_file_name):
    with open(html_file_name, 'rt') as f:
        html = f.read()

    bsObj = BeautifulSoup(html, 'html.parser')
    results = bsObj.find_all('div', class_='results')[0]
    total_number = results.find_all('h2')[0].text
    rows = results.find_all('dl')
    table = []
    for i, r in enumerate(rows):
        name = r.a.text
        # category = r.a.next_sibling.
        category = 'music'
        verfied, age, size, peers, leech = list(map(lambda x: x.text, r.find_all('span')))
        if verfied:
            verfied = 'Y'
        else:
            verfied = ' '

        table.append((i, name, category, verfied, age, size, peers, leech))
        # print('[{0}]: {1}'.format(i, name))

    return total_number, table
