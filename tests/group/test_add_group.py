# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application


def test_add_group(app):
    app.group.create(Group(name="New group",
                           header="Group header",
                           footer="Group footer"))


def test_add_empty_group(app):
    app.group.create(Group(name="",
                           header="",
                           footer=""))
