import click

from .model import Result, Browser

from .utils import ptable, magnetize, urlize
from .user_input import proccess_command


@click.command()
@click.argument('search',  nargs=-1, required=False)
@click.option('--verified', '-v', is_flag=True, help='Search only for verified torrents')
@click.option('--adult', '-a', is_flag=True, help='Search only for safe torrents')
@click.option('--limit-rows', '-l', default=25, help='Limit the number of output rows')
@click.option('--sort-by', type=click.Choice(['peers', 'date', 'rating', 'size']))
def main(**kwargs):
    """seach and get infohash from torrentz2.eu"""
    search_url = urlize(**kwargs)
    limit_rows = kwargs['limit_rows']
    process_demand(search_url, limit_rows)


def process_demand(search_url, limit_rows):
    # click.echo('downloading ...')
    driver = Browser(search_url)
    driver.get(search_url)
    # click.echo('parsing ...')
    results = driver.parse_search_page()
    print(len(results))
    for i in range(len(results)):
        print(i, results[i].name)
    # ptable(table, limit_rows=limit_rows)
    while True:
        requests = proccess_command(input(':: '))
        if requests is None:
            continue
        else:
            # append magnets to file
            for i in requests:
                click.echo('Downloading #{}'.format(i))
                html_text = driver.get(results[i].link)
                driver.parse_torrent_page(results[i])
                print('LINK:', result[i].magnet)
