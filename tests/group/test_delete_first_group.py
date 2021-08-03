# -*- coding: utf-8 -*-
def test_delete_group(app):
    app.main_url()
    app.session.login(user="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()
