import pytest
from tz2 import api 


def test_api_blank():
    with pytest.raises(KeyError):
        data = {}
        api.urlize(**data)


def test_api_normal():
    data = {'search': (), 'verified': False, 'adult': False, 'limit_rows': None, 'sort_by': None}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/search?f=&safe=1'


def test_api_w_verfied_option_no_arg():
    data = {'search': (), 'verified': True, 'adult': False, 'limit_rows': None, 'sort_by': None}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/verified?f=&safe=1'

def test_api_w_adult_and_one_arg():
    data = {'search': ('archlinux',), 'verified': False, 'adult': True, 'limit_rows': None, 'sort_by': None}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/search?f=archlinux&safe=0'


def test_api_w_verfied_option_one_arg():
    data = {'search': ('archlinux',), 'verified': True, 'adult': False, 'limit_rows': None, 'sort_by': None}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/verified?f=archlinux&safe=1'


def test_api_wo_option_one_arg():
    data = {'search': ('archlinux',), 'verified': False, 'adult': False, 'limit_rows': None, 'sort_by': None}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/search?f=archlinux&safe=1'


def test_api_w_sort_by_date_and_one_arg():
    data = {'search': ('archlinux',), 'verified': False, 'adult': False, 'limit_rows': None, 'sort_by': 'date'}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/searchA?f=archlinux&safe=1'


def test_api_w_sort_by_size_and_one_arg():
    data = {'search': ('archlinux',), 'verified': False, 'adult': False, 'limit_rows': None, 'sort_by': 'size'}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/searchS?f=archlinux&safe=1'


def test_api_w_sort_by_peers_and_one_arg():
    data = {'search': ('archlinux',), 'verified': False, 'adult': False, 'limit_rows': None, 'sort_by': 'peers'}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/search?f=archlinux&safe=1'


def test_api_w_sort_by_peers_verified_and_one_arg():
    data = {'search': ('archlinux',), 'verified': True, 'adult': False, 'limit_rows': None, 'sort_by': 'peers'}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/verifiedP?f=archlinux&safe=1'


def test_api_w_sort_by_rating_and_one_arg():
    data = {'search': ('archlinux',), 'verified': False, 'adult': False, 'limit_rows': None, 'sort_by': 'rating'}
    result = api.urlize(**data)
    assert result == 'https://torrentz2.eu/searchN?f=archlinux&safe=1'
