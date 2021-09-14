# -*- coding: utf-8 -*-
from model.group import Group
import random


# from random import randrange
# import pytest
# from data.groups import testdata
#
#
# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])


def test_update_rnd_group_name(app, db, json_groups, check_ui):
    group = json_groups
    if db.get_group_list() == 0:
        app.group.create(Group(name="Create group for Updated"))
    old_groups = db.get_group_list()
    changed_group = random.choice(old_groups)
    new_group = group
    new_group.id = changed_group.id
    app.group.update_group_by_id(changed_group.id, new_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups.remove(changed_group)
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group_cl):
            return Group(id=group_cl.id, name=group_cl.name.strip())

        assert sorted(app.group.get_group_list(), key=Group.id_or_max)\
               == sorted(list(map(clean, old_groups)), key=Group.id_or_max)\
               == sorted(list(map(clean, new_groups)), key=Group.id_or_max)
