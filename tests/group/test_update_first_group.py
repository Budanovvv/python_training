# -*- coding: utf-8 -*-
from model.group import Group


def test_update_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Create group for Updated"))
    app.group.update_first_group(Group(name="Updated group2"))


def test_update_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Create group for Updated"))
    app.group.update_first_group(Group(header="Updated header2"))


def test_update_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Create group for Updated"))
    app.group.update_first_group(Group(footer="Updated footer2"))

