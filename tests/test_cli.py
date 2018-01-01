import pytest
from click.testing import CliRunner
from tz2 import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_blank(runner):
    result = runner.invoke(cli.main)
    assert not result.exception
    assert result.exit_code == 0
    assert result.output.split('\n', 1)[0].strip() == 'https://torrentz2.eu/search?f=&safe=1'


def test_cli_w_verfied_option_no_arg(runner):
    result = runner.invoke(cli.main, ['-v'])
    assert not result.exception
    assert result.exit_code == 0
    assert result.output.split('\n', 1)[0].strip() == 'https://torrentz2.eu/verified?f=&safe=1'


def test_cli_w_adult_and_one_arg(runner):
    result = runner.invoke(cli.main, ['-a', 'archlinux'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.split('\n', 1)[0].strip() == 'https://torrentz2.eu/search?f=archlinux&safe=0'


def test_cli_w_verfied_option_one_arg(runner):
    result = runner.invoke(cli.main, ['--verified', 'archlinux'])
    assert not result.exception
    assert result.exit_code == 0
    assert result.output.split('\n', 1)[0].strip() == 'https://torrentz2.eu/verified?f=archlinux&safe=1'


def test_cli_wo_option_one_arg(runner):
    result = runner.invoke(cli.main, ['archlinux'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.split('\n', 1)[0].strip() == 'https://torrentz2.eu/search?f=archlinux&safe=1'


def test_cli_w_sort_by_date_and_one_arg(runner):
    result_date = runner.invoke(cli.main, ['--sort-by', 'date', 'archlinux'])
    assert result_date.exit_code == 0
    assert not result_date.exception
    assert result_date.output.split('\n', 1)[0].strip() == 'https://torrentz2.eu/searchA?f=archlinux&safe=1'


def test_cli_w_sort_by_size_and_one_arg(runner):
    result_size = runner.invoke(cli.main, ['--sort-by', 'size', 'archlinux'])
    assert result_size.exit_code == 0
    assert not result_size.exception
    assert result_size.output.split('\n', 1)[0].strip() == 'https://torrentz2.eu/searchS?f=archlinux&safe=1'


def test_cli_w_sort_by_peers_and_one_arg(runner):
    result_peers = runner.invoke(cli.main, ['--sort-by', 'peers', 'archlinux'])
    assert result_peers.exit_code == 0
    assert not result_peers.exception
    assert result_peers.output.split('\n', 1)[0].strip() == 'https://torrentz2.eu/search?f=archlinux&safe=1'


def test_cli_w_sort_by_peers_verified_and_one_arg(runner):
    result_peers = runner.invoke(cli.main, ['-v', '--sort-by', 'peers', 'archlinux'])
    assert result_peers.exit_code == 0
    assert not result_peers.exception
    assert result_peers.output.split('\n', 1)[0].strip() == 'https://torrentz2.eu/verifiedP?f=archlinux&safe=1'


def test_cli_w_sort_by_ranking_and_one_arg(runner):
    result_ranking = runner.invoke(cli.main, ['--sort-by', 'rating', 'archlinux'])
    assert result_ranking.exit_code == 0
    assert not result_ranking.exception
    assert result_ranking.output.split('\n', 1)[0].strip() == 'https://torrentz2.eu/searchN?f=archlinux&safe=1'
