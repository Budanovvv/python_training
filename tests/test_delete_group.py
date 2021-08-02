# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_delete_group(app):
    app.home_page()
    app.session.login(user="admin", password="secret")
    app.group.delete()
    app.session.logout()
