# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits\
              # + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# testdata = [
#     Group(name=name, header=header, footer=header)
#     for name in ["", random_string("name ", 10)]
#     for header in ["", random_string("header ", 20)]
#     for footer in ["", random_string("footer ", 20)]
# ]


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name - ", 10),
          header=random_string("header - ", 10),
          footer=random_string("footer - ", 10))
    for i in range(5)
]


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

