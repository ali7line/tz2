import click


def pretty_table(table):
    click.echo("{0:>4} | {1:^40} | {2:^5} | {3:^5} | {4:^10} | {5:^8} | {6:^6} | {7:^6}".format(
        'id', 'name', 'cat', 'verif', 'age', 'size', 'peers', 'leech'))
    click.echo("-"*(4+40+5+5+10+8+6+6+21))
    for id_, name, cat, verif, age, size, peers, leech, links in table:
        click.echo("{0:>4} | {1:^40} | {2:<5} | {3:^5} | {4:<10} | {5:<8} | {6:^6} | {7:^6}".format(
            id_, name[:40], cat, verif, age, size, peers, leech))
