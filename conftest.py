# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
import json
import os.path


fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        path_to_config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(path_to_config_file) as opened_config_file:
            target = json.load(opened_config_file)
    if fixture is None or not fixture.is_valid:
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_login(user=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")