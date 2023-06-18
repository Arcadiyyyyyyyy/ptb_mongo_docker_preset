from ptb_mongo_docker_preset.utils.custom_middleware import perhaps
from ptb_mongo_docker_preset import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_perhaps():
    assert perhaps() == 1
    assert perhaps() != 0
