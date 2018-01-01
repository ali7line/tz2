import click

from .utils.pretty_table import pretty_table
from .utils.url import parse_search, get_url


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
            if verified:
                search_suffix = 'P'
            else:
                search_suffix = ''
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
        safe_suffix = '&safe=1'

    search_url = 'https://torrentz2.eu/{0}{1}?f={2}{3}'.format(
        search_type,
        search_suffix,
        '+'.join(search),
        safe_suffix)

    click.echo(search_url)
    click.echo('downloading ...')
    html_text = get_url(search_url)
    click.echo('parsing ...')
    total, table = parse_search(html_text)

    click.echo(total)
    pretty_table(table)
