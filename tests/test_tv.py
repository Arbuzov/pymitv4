from pymitv4.control import Control
from pymitv4.navigator import Navigator
from pymitv4.tv import TV


def test_is_on_with_assumed_state(monkeypatch):
    monkeypatch.setattr(Control, "check_state", lambda self, ip: True)
    monkeypatch.setattr(Control, "get_volume", lambda self, ip: 5)
    tv = TV(ip_address="1.2.3.4", assume_state=True)
    tv.state = False
    assert tv.is_on is False


def test_is_on_without_assumed_state(monkeypatch):
    monkeypatch.setattr(Control, "check_state", lambda self, ip: True)
    monkeypatch.setattr(Control, "get_volume", lambda self, ip: 5)
    tv = TV(ip_address="1.2.3.4", assume_state=False)
    assert tv.is_on is True


def test_set_source(monkeypatch):
    monkeypatch.setattr(Control, "get_volume", lambda self, ip: 5)
    tv = TV(ip_address="1.2.3.4")
    monkeypatch.setattr(
        Navigator,
        "navigate_to_source",
        lambda self, s: ["enter"],
    )

    called = {}

    def fake_send(self, keystrokes, wait=False):
        called["args"] = (keystrokes, wait)
        return True

    monkeypatch.setattr(TV, "_send_keystroke", fake_send)

    result = tv.set_source("hdmi1")
    assert result is True
    assert called["args"] == (["enter"], True)
