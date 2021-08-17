# -*- coding: utf-8 -*-
from model.group import Group


def test_update_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Create group for Updated"))
    old_groups = app.group.get_group_list()
    group = Group(name="Updated group2")
    group.group_id = old_groups[0].group_id
    app.group.update_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_update_first_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Create group for Updated"))
#     old_groups = app.group.get_group_list()
#     group = Group(header="Updated header2")
#     group.group_id = old_groups[0].group_id
#     app.group.update_first_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_update_first_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Create group for Updated"))
#     old_groups = app.group.get_group_list()
#     group = Group(header="Updated footer2")
#     group.group_id = old_groups[0].group_id
#     app.group.update_first_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)