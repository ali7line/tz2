import pytest
from click.testing import CliRunner
from tz2 import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_with_verfied_option(runner):
    result = runner.invoke(cli.main, ['--verfied', 'Ali'])
    assert not result.exception
    assert result.exit_code == 0
    assert result.output.strip() == 'https://torrentz2.eu/verfied?f=Ali'


def test_cli_with_no_option_and_one_arg(runner):
    result = runner.invoke(cli.main, ['Ali'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'https://torrentz2.eu/search?f=Ali'
