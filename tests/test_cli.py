from aicodebot.cli import fun_fact, version
from click.testing import CliRunner
from setup import __version__
import os, pytest


def test_version():
    runner = CliRunner()
    result = runner.invoke(version)
    assert result.exit_code == 0
    assert __version__ in result.output


@pytest.mark.skipif(os.getenv("OPENAI_API_KEY") is None, reason="Skipping live tests without an API key.")
def test_funfact():
    runner = CliRunner()
    result = runner.invoke(fun_fact)
    assert result.exit_code == 0