import pytest


PARAMS = [
    ('mtu', '65536'),
    ('inet4', ['127.0.0.1']),
    ('inet6', ['::1']),
]


@pytest.mark.parametrize(['test_key', 'expected_value'], PARAMS)
def test_ifconfig_lo_interface(test_key, expected_value, get_ifconfig_lo_interface):
    assert get_ifconfig_lo_interface[test_key] == expected_value
