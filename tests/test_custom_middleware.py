from ptb_mongo_docker_preset.utils.custom_middleware import perhaps


def test_perhaps():
    assert perhaps() == 1
    assert perhaps() != 0
