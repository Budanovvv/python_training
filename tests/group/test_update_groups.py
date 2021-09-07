# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import pytest
from data.groups import testdata


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_update_rnd_group_name(app, group):
    if app.group.count() == 0:
        app.group.create(Group(name="Create group for Updated"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.update_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

