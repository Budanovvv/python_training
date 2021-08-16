# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Create group for delete"))
    old_group = app.group.get_group_list()
    app.group.delete_first_group()
    new_group = app.group.get_group_list()
    assert len(old_group) - 1 == len(new_group)
    old_group[0:1] = []
    assert old_group == new_group
