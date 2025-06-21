from pymitv4.control import Control


class DummyResponse:
    def __init__(self, status_code=200, data='{"volum":10}'):
        self.status_code = status_code
        self._data = data

    def json(self):
        return {"data": self._data}


def test_get_volume_success(monkeypatch):
    def fake_get(url, timeout):
        return DummyResponse(200, '{"volum":5}')

    monkeypatch.setattr("requests.get", fake_get)

    assert Control.get_volume("1.2.3.4") == 5


def test_get_volume_failure(monkeypatch):
    def fake_get(url, timeout):
        from requests.exceptions import ConnectionError

        raise ConnectionError()

    monkeypatch.setattr("requests.get", fake_get)

    assert Control.get_volume("1.2.3.4") is False
