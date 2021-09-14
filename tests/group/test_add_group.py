# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group_cl):
            return Group(id=group_cl.id, name=group_cl.name.strip())

        assert sorted(app.group.get_group_list(), key=Group.id_or_max)\
               == sorted(list(map(clean, old_groups)), key=Group.id_or_max)\
               == sorted(list(map(clean, new_groups)), key=Group.id_or_max)