# -*- coding: utf-8 -*-
from model.group import Group


def test_update_first_group_name(app):
    app.group.update_first_group(Group(name="Updated group2"))


def test_update_first_group_header(app):
    app.group.update_first_group(Group(header="Updated header2"))


def test_update_first_group_footer(app):
    app.group.update_first_group(Group(footer="Updated footer2"))

