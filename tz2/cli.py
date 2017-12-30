from beautifultable import BeautifulTable
from bs4 import BeautifulSoup
import click


def parse(html_file_name):
    col = 30

    with open(html_file_name, 'r') as f:
        html = f.read()

    bsObj = BeautifulSoup(html, 'html.parser')
    results = bsObj.find_all('div', class_='results')[0]
    total_number = results.find_all('h2')[0].text
    rows = results.find_all('dl')
    table = BeautifulTable()
    table.column_headers = ["id", "name", "cat", "verif", "age", "size", "peers", "leech"]
    for i, r in enumerate(rows):
        name = r.a.text
        category = r.a.next_sibling
        verfied, age, size, peers, leech = list(map(lambda x: x.text, r.find_all('span')))
        table.append_row((i, name[:col], category, verfied, age, size, peers, leech))
        # print('[{0}]: {1}'.format(i, name))

    click.echo(table)

    return total_number


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
    total = parse('/tmp/torrent.html')
    click.echo(total)
