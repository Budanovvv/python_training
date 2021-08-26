# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_delete_rnd_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Create group for delete"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups[index:index+1] = []
    assert old_groups == new_groups


def test_delete_all_groups(app):
    app.group.test_delete_all_groups()
    assert app.group.count() == 0
