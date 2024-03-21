import urllib.request

import pytest


def test_needs_internet(needs_internet):
    """
    This test should always succeed or be skipped.
    """
    urllib.request.urlopen('http://pypi.org/')


@pytest.mark.network
def test_network_marker():
    """
    This test should always succeed or be skipped.
    """
    urllib.request.urlopen('http://pypi.org/')
