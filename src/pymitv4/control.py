"""The ``pymitv4.control`` module sends keystrokes to the TV."""
import json
import time

import requests


class Control:
    """A virtual remote control for the TV."""
    turn_on = ['power']
    turn_off = ['power']
    sleep = ['power', 'wait', 'right', 'wait', 'right', 'wait', 'enter']
    wake = ['power']
    up = ['up']
    down = ['down']
    right = ['right']
    left = ['left']
    home = ['home']
    enter = ['enter']
    back = ['back']
    menu = ['menu']
    volume_down = ['volumedown']
    volume_up = ['volumeup']

    def __init__(self):
        print()

    @staticmethod
    def send_keystrokes(ip_address, keystrokes, wait=False):
        """Connects to TV and sends keystroke via HTTP."""
        tv_url = (
            f"http://{ip_address}:6095/controller?action=keyevent&keycode="
        )

        for keystroke in keystrokes:
            if keystroke == 'wait' or wait is True:

                time.sleep(0.7)
            else:
                request = requests.get(tv_url + keystroke)

                if request.status_code != 200:
                    return False

        return True

    @staticmethod
    def change_source(ip_address, source):
        """Select source hdmi1 or hdmi2"""
        tv_url = (
            f"http://{ip_address}:6095/controller?action=changesource&source="
        )
        source = source
        request = requests.get(tv_url + source)
        if request.status_code != 200:
            return False

        return True

    @staticmethod
    def mute(ip_address):
        """Polyfill for muting the TV."""
        tv_url = (
            f"http://{ip_address}:6095/controller?action=keyevent&keycode="
        )

        count = 0
        while count > 30:
            count = count + 1
            request = requests.get(tv_url + 'volumedown')

            if request.status_code != 200:
                return False

        return True

    @staticmethod
    def check_state(ip_address):
        """Check if xiaomi tv is reachable"""
        request_timeout = 0.1

        try:
            tv_url = f"http://{ip_address}:6095/request?action=isalive"
            requests.get(tv_url, timeout=request_timeout)
        except (
            requests.exceptions.ConnectTimeout,
            requests.exceptions.ConnectionError,
        ):
            return False

        return True

    @staticmethod
    def get_volume(ip_address):
        """Get the current volume of xiaomi tv"""
        request_timeout = 0.1

        try:
            tv_url = f"http://{ip_address}:6095/general?action=getVolum"
            request = requests.get(tv_url, timeout=request_timeout)
        except (
            requests.exceptions.ConnectTimeout,
            requests.exceptions.ConnectionError,
        ):
            return False

        volume = json.loads(request.json()['data'])['volum']
        return volume

    @staticmethod
    def get_system_info(ip_address):
        """Return system information for the TV."""
        tv_url = f"http://{ip_address}:6095/controller?action=getsysteminfo"
        request = requests.get(tv_url)
        if request.status_code != 200:
            return None
        return request.json()

    @staticmethod
    def capture_screen(ip_address):
        """Capture the current TV screen and return the raw response."""
        tv_url = f"http://{ip_address}:6095/controller?action=capturescreen"
        request = requests.get(tv_url)
        if request.status_code != 200:
            return None
        return request.content

    @staticmethod
    def get_installed_apps(ip_address, count=999, change_icon=1):
        """Return list of installed applications."""
        tv_url = (
            f"http://{ip_address}:6095/controller?"
            f"action=getinstalledapp&count={count}&changeIcon={change_icon}"
        )
        request = requests.get(tv_url)
        if request.status_code != 200:
            return None
        return request.json()

    @staticmethod
    def get_apps(ip_address):
        """Compatibility wrapper for ``get_installed_apps``."""
        apps = Control.get_installed_apps(ip_address)
        if apps is None:
            return False
        return apps.get('data') if isinstance(apps, dict) else apps

    @staticmethod
    def start_app(ip_address, package_name, app_type='packagename'):
        """Start an application on the TV."""
        tv_url = (
            'http://{}:6095/controller?action=startapp&type={}&packagename={}'
        ).format(ip_address, app_type, package_name)
        request = requests.get(tv_url)
        if request.status_code != 200:
            return False
        return True
