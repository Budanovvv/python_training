# -*- coding: utf-8 -*-
from model.group import Group


def test_update_first_group(app):
    app.home_page()
    app.session.login(user="admin", password="secret")
    app.group.update_first_group(Group(name="Updated group",
                                       header="Updated header",
                                       footer="Updated footer"))
    app.session.logout()
