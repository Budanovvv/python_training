# -*- coding: utf-8 -*-
from model.group import Group


def test_update_first_group_name(app):
    app.main_url()
    app.session.login(user="admin", password="secret")
    app.group.update_first_group(Group(name="Updated group2"))
    app.session.logout()


def test_update_first_group_header(app):
    app.main_url()
    app.session.login(user="admin", password="secret")
    app.group.update_first_group(Group(header="Updated header2"))
    app.session.logout()


def test_update_first_group_footer(app):
    app.main_url()
    app.session.login(user="admin", password="secret")
    app.group.update_first_group(Group(footer="Updated footer2"))
    app.session.logout()
