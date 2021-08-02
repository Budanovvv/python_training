# -*- coding: utf-8 -*-
from model.group import Group
<<<<<<< HEAD:tests/group/test_add_group.py
=======
from fixture.application_group import Application_group
import pytest


@pytest.fixture
def app(request):
    fixture = Application_group()
    request.addfinalizer(fixture.destroy)
    return fixture
>>>>>>> Budanovvv:tests/test_add_group.py


def test_add_group(app):
    app.home_page()
    app.session.login(user="admin", password="secret")
    app.group.create(Group(name="New group",
                           header="Group header",
                           footer="Group footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.home_page()
    app.session.login(user="admin", password="secret")
    app.group.create(Group(name="",
                           header="",
                           footer=""))
    app.session.logout()
