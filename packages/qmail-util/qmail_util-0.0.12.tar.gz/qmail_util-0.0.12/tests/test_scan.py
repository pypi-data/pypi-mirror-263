import os

import pytest

from qmail_util.main import Session, Sessions, scan

MAILSERVER1 = os.environ["MAILSERVER1"]
MAILSERVER2 = os.environ["MAILSERVER2"]


@pytest.fixture
def check_result():
    def _check_result(result):
        assert isinstance(result, Sessions)
        assert isinstance(result.total, Session)
        assert result.total.count
        assert result.total.count == result.total.ok + result.total.fail
        for session in result.sessions.values():
            assert isinstance(session, Session)
            assert session.count == session.ok + session.fail
        return True

    return _check_result


def test_scan_default(check_result):
    result = scan(MAILSERVER1)
    assert check_result(result)


def test_scan_all(check_result):
    result = scan(MAILSERVER1, all=True)
    assert check_result(result)


def test_scan_multiple(check_result):
    first = scan(MAILSERVER1)
    assert check_result(first)
    second = scan(MAILSERVER2)
    assert check_result(second)
