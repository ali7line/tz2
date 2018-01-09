import pytest

from tz2 import api


def test_urlize_blank():
    with pytest.raises(KeyError):
        data = {}
        api.urlize(**data)


def test_urlize_normal():
    data = {'search': (), 'verified': False, 'adult': False, 'limit_rows': None, 'sort_by': None}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/search?f=&safe=1'


def test_urlize_w_verfied_option_no_arg():
    data = {'search': (), 'verified': True, 'adult': False, 'limit_rows': None, 'sort_by': None}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/verified?f=&safe=1'


def test_urlize_w_adult_and_one_arg():
    data = {'search': ('archlinux',), 'verified': False, 'adult': True, 'limit_rows': None, 'sort_by': None}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/search?f=archlinux&safe=0'


def test_urlize_w_verfied_option_one_arg():
    data = {'search': ('archlinux',), 'verified': True, 'adult': False, 'limit_rows': None, 'sort_by': None}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/verified?f=archlinux&safe=1'


def test_urlize_wo_option_one_arg():
    data = {'search': ('archlinux',), 'verified': False, 'adult': False, 'limit_rows': None, 'sort_by': None}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/search?f=archlinux&safe=1'


def test_urlize_wo_option_two_arg():
    data = {'search': ('archlinux', '2017',), 'verified': False, 'adult': False, 'limit_rows': None, 'sort_by': None}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/search?f=archlinux+2017&safe=1'


def test_urlize_w_sort_by_date_and_one_arg():
    data = {'search': ('archlinux',), 'verified': False, 'adult': False, 'limit_rows': None, 'sort_by': 'date'}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/searchA?f=archlinux&safe=1'


def test_urlize_w_sort_by_size_and_one_arg():
    data = {'search': ('archlinux',), 'verified': False, 'adult': False, 'limit_rows': None, 'sort_by': 'size'}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/searchS?f=archlinux&safe=1'


def test_urlize_w_sort_by_peers_and_one_arg():
    data = {'search': ('archlinux',), 'verified': False, 'adult': False, 'limit_rows': None, 'sort_by': 'peers'}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/search?f=archlinux&safe=1'


def test_urlize_w_sort_by_peers_verified_and_one_arg():
    data = {'search': ('archlinux',), 'verified': True, 'adult': False, 'limit_rows': None, 'sort_by': 'peers'}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/verifiedP?f=archlinux&safe=1'


def test_urlize_w_sort_by_rating_and_one_arg():
    data = {'search': ('archlinux',), 'verified': False, 'adult': False, 'limit_rows': None, 'sort_by': 'rating'}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/searchN?f=archlinux&safe=1'


def test_magnetize_normal():
    hashinfo = '204a1789dd04e4d8f5a4e098e8f777794888f4ad'
    trackers = (
            'udp://tracker.coppersurfer.tk:6969/announce', 'http://68.64.165.106:2710/announce',
            'http://p4p.arenabg.ch:1337/announce', 'http://tracker.internetwarriors.net:1337/announce',
            'udp://tracker.vanitycore.co:6969/announce', 'udp://tracker.leechers-paradise.org:6969/announce',
            'udp://p4p.arenabg.ch:1337/announce',
            )
    result = api.magnetize(hashinfo, trackers)
    assert result == 'magnet:?xt=urn:btih:204a1789dd04e4d8f5a4e098e8f777794888f4ad' + \
        '&tr=udp://tracker.coppersurfer.tk:6969/announce&tr=http://68.64.165.106:2710/announce' + \
        '&tr=http://p4p.arenabg.ch:1337/announce&tr=http://tracker.internetwarriors.net:1337/announce' + \
        '&tr=udp://tracker.vanitycore.co:6969/announce&tr=udp://tracker.leechers-paradise.org:6969/announce' + \
        '&tr=udp://p4p.arenabg.ch:1337/announce'


def test_magnetize_no_tracker():
    hashinfo = '204a1789dd04e4d8f5a4e098e8f777794888f4ad'
    result = api.magnetize(hashinfo)
    assert result == 'magnet:?xt=urn:btih:204a1789dd04e4d8f5a4e098e8f777794888f4ad'
