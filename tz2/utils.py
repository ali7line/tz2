import click
import re

def urlize(**kwargs):

    if kwargs['search']:
        search = kwargs['search']
    else:
        search = ''

    if kwargs['verified']:
        search_type = 'verified'
    else:
        search_type = 'search'

    if kwargs['sort_by']:
        if kwargs['sort_by'] == 'peers':
            if search_type == 'verified':
                search_suffix = 'P'
            else:
                search_suffix = ''
        if kwargs['sort_by'] == 'date':
            search_suffix = 'A'
        if kwargs['sort_by'] == 'rating':
            search_suffix = 'N'
        if kwargs['sort_by'] == 'size':
            search_suffix = 'S'
    else:
        search_suffix = ''

    if kwargs['adult']:
        safe_suffix = '&safe=0'
    else:
        safe_suffix = '&safe=1'

    return 'https://torrentz2.eu/{0}{1}?f={2}{3}'.format(
        search_type,
        search_suffix,
        '+'.join(search),
        safe_suffix)

def remove_nonlatin(text):
    return re.sub(r'[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]', '', str(text))


def ptable(table, limit_rows=25):
    width = {'w_id': 4, 'w_name': 60, 'w_cat': 25, 'w_verif': 5, 'w_age': 10, 'w_size': 8, 'w_peers': 6, 'w_leech': 6}
    total_width = sum(width.values()) + 3*8

    row = "{id_:>{w_id}} | {name:^{w_name}} | {cat:^{w_cat}} | {verif:^{w_verif}} | " + \
        "{age:^{w_age}} | {size:^{w_size}} | {peers:^{w_peers}} | {leech:^{w_leech}}"

    data = {'id_': 'id', 'name': 'name', 'cat': 'cat', 'verif': 'verif', 'age': 'age', 'size': 'size',
            'peers': 'peers', 'leech': 'leech'}

    z = {**data, **width}

    click.echo(row.format(**z))

    click.echo("-"*total_width)
    if len(table) > limit_rows:
        table = table[:limit_rows]

    for id_, name, cat, verif, age, size, peers, leech, links in table:
        cat = remove_nonlatin(cat)

        name = remove_nonlatin(name)
        if len(name) > 40:
            name = name[:40]

        data = {'id_': id_, 'name': name, 'cat': cat, 'verif': verif, 'age': age,
                'size': size, 'peers': peers, 'leech': leech}
        z = {**data, **width}

        click.echo(row.format(**z))


def magnetize(hashinfo, trackers=None):
    if not hashinfo.isalnum():
        raise ValueError('invalid characters in hashinfo')

    if len(hashinfo) != 40:
        raise ValueError('invalid number of characters in hashinfo')

    if trackers:
        trackinfo = '&tr=' + '&tr='.join(trackers)
    else:
        trackinfo = ''

    return 'magnet:?xt=urn:btih:' + hashinfo + trackinfo
