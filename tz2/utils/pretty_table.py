import click
import re


def remove_nonlatin(text):
    return re.sub(r'[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]', '', str(text))


def pretty_table(table, limit_rows=25):
    click.echo("{0:>4} | {1:^40} | {2:^25} | {3:^5} | {4:^10} | {5:^8} | {6:^6} | {7:^6}".format(
        'id', 'name', 'cat', 'verif', 'age', 'size', 'peers', 'leech'))
    click.echo("-"*(4+40+5+5+10+8+6+6+21+20))
    if len(table) > limit_rows:
        table = table[:limit_rows]
    for id_, name, cat, verif, age, size, peers, leech, links in table:
        new_cat = remove_nonlatin(cat)
        new_name = remove_nonlatin(name)
        if len(name) > 40:
            click.echo("{0:>4} | {1:^40} | {2:<25} | {3:^5} | {4:<10} | {5:<8} | {6:^6} | {7:^6}".format(
                id_, new_name[:40], new_cat, verif, age, size, peers, leech))
        else:
            click.echo("{0:>4} | {1:^40} | {2:<25} | {3:^5} | {4:<10} | {5:<8} | {6:^6} | {7:^6}".format(
                id_, new_name, new_cat, verif, age, size, peers, leech))
