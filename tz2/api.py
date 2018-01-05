def urlize(**kwargs):
    # def urlize(search, verified, adult, sort_by, limit_rows):
    print(kwargs)

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
        if kwargs['sort_by']== 'size':
            search_suffix = 'S'
    else:
        search_suffix = ''


    if kwargs['adult']:
        safe_suffix = '&safe=0'
    else:
        safe_suffix = '&safe=1'

    search_url = 'https://torrentz2.eu/{0}{1}?f={2}{3}'.format(
        search_type,
        search_suffix,
        '+'.join(search),
        safe_suffix)

    return search_url


def download(url):
    pass


def magnetize():
    pass
