# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_update_group(app):
    app.home_page()
    app.session.login(user="admin", password="secret")
    app.group.update(Group(name="Updated group",
                           header="Updated header",
                           footer="Updated footer"))
    app.session.logout()
