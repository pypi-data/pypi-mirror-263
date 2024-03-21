import urllib.request

import pytest
import jaraco.functools
from jaraco.context import ExceptionTrap


@jaraco.functools.once
def has_internet():
    """
    Is this host able to reach the Internet?

    Return True if the internet appears reachable and False
    otherwise.
    """
    with ExceptionTrap() as trap:
        urllib.request.urlopen('http://pypi.org')
    return not trap


def check_internet():
    """
    (pytest) Skip if internet is unavailable.
    """
    has_internet() or pytest.skip('Internet connectivity unavailable')


@pytest.fixture
def needs_internet():
    """
    Pytest fixture signaling that internet is required.
    """
    check_internet()


def pytest_configure(config):
    """
    Register the 'network' marker.
    """
    config.addinivalue_line(
        "markers", "network: the test requires network connectivity"
    )


def pytest_runtest_setup(item):
    """
    For any tests marked with 'network', install fixture.
    """
    for marker in item.iter_markers(name='network'):
        item.fixturenames.extend({'needs_internet'} - set(item.fixturenames))
