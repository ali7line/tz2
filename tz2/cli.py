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
    html_text, browser = get_url(search_url)
    # click.echo('parsing ...')
    total, table = parse_search(html_text)

    click.echo(total)
    ptable(table, limit_rows=limit_rows)
    while True:
        result = proccess_command(input(':: '))
        if result is None:
            continue
        else:
            # append magnets to file
            for i in result:
                click.echo('Downloading #{}'.format(i))
                print(table[int(i)])
                html_text = get_url(table[int(i)][-1], browser)
                hashinfo, trackers = parse_link(html_text)
                print('LINK:', magnetize(hashinfo, trackers))
