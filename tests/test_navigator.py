from pymitv4.navigator import Navigator


def test_navigate_without_source():
    nav = Navigator()
    route = nav.navigate_to_source("hdmi2")
    expected = nav.OPEN_SOURCES_IF_NONE + nav.SOURCE_PATH["hdmi2"]
    assert route == expected


def test_navigate_with_source():
    nav = Navigator(source="hdmi1")
    route = nav.navigate_to_source("hdmi2")
    expected = nav.OPEN_SOURCES_IF_SOURCE_ACTIVE + nav.SOURCE_PATH["hdmi2"]
    assert route == expected
