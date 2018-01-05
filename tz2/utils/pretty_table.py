import click
import re


def remove_nonlatin(text):
    return re.sub(r'[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]', '', str(text))


def pretty_table(table, limit_rows=25):
    width = {'w_id': 4, 'w_name': 40, 'w_cat': 25, 'w_verif': 5, 'w_age': 10, 'w_size': 8, 'w_peers': 6, 'w_leech': 6}
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
