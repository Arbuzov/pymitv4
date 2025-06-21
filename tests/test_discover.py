from pymitv4.discover import Discover


class DummyResponse:
    def __init__(self, status_code=200):
        self.status_code = status_code
        self._json = {"data": "{}"}

    def json(self):
        return self._json


def test_check_ip_success(monkeypatch):
    def fake_get(url, timeout):
        return DummyResponse(200)

    monkeypatch.setattr("requests.get", fake_get)

    assert Discover.check_ip("1.2.3.4") is True


def test_check_ip_failure(monkeypatch):
    def fake_get(url, timeout):
        from requests.exceptions import ConnectionError

        raise ConnectionError("connection error")

    monkeypatch.setattr("requests.get", fake_get)

    assert Discover.check_ip("1.2.3.4") is False
