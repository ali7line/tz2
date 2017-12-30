from bs4 import BeautifulSoup
import click


def pretty_table(table):
    click.echo("{0:>4} | {1:^40} | {2:^5} | {3:^5} | {4:^10} | {5:^8} | {6:^6} | {7:^6}".format(
        'id', 'name', 'cat', 'verif', 'age', 'size', 'peers', 'leech'))
    del table[0]
    for id_, name, cat, verif, age, size, peers, leech in table:
        click.echo("{0:>4} | {1:^40} | {2:<5} | {3:^5} | {4:<10} | {5:<8} | {6:^6} | {7:^6}".format(
            id_, name[:40], cat, verif, age, size, peers, leech))


def parse(html_file_name):
    with open(html_file_name, 'rt') as f:
        html = f.read()

    bsObj = BeautifulSoup(html, 'html.parser')
    results = bsObj.find_all('div', class_='results')[0]
    total_number = results.find_all('h2')[0].text
    rows = results.find_all('dl')
    table = []
    table.append(("id", "name", "cat", "verif", "age", "size", "peers", "leech"))
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


@click.command()
@click.argument('search',  nargs=-1, required=False)
@click.option('--verified', '-v', is_flag=True, help='Search only for verified torrents')
@click.option('--adult', '-a', is_flag=True, help='Search only for safe torrents')
@click.option('--sort-by', type=click.Choice(['peers', 'date', 'rating', 'size']))
def main(search, verified, adult, sort_by):
    """seach and get infohash from torrentz2.eu"""
    click.clear()

    if not search:
        search = ''

    if verified:
        search_type = 'verified'
    else:
        search_type = 'search'

    if sort_by:
        if sort_by == 'peers':
            search_suffix = 'P'
        if sort_by == 'date':
            search_suffix = 'A'
        if sort_by == 'rating':
            search_suffix = 'N'
        if sort_by == 'size':
            search_suffix = 'S'
    else:
        search_suffix = ''

    if adult:
        safe_suffix = '&safe=0'
    else:
        safe_suffix = ''

    click.echo('https://torrentz2.eu/{0}{1}?f={2}{3}'.format(
        search_type,
        search_suffix,
        '+'.join(search),
        safe_suffix)
        )
    click.echo('downloading ...')
    click.echo('parsing ...')
    total, table = parse('/tmp/torrent.html')
    click.echo(total)
    pretty_table(table)
