import click


@click.command()
@click.argument('search',  nargs=-1, required=True)
@click.option('--verfied', '-v', is_flag=True, help='Search only for verfied torrents')
@click.option('--adult', '-a', is_flag=True, help='Search only for safe torrents')
@click.option('--sort-by', type=click.Choice(['peers', 'date', 'rating', 'size']))
def main(search, verfied, adult, sort_by):
    """seach and get infohash from torrentz2.eu"""
    if verfied:
        search_type = 'verfied'
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
