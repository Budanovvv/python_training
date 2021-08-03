# -*- coding: utf-8 -*-
def test_delete_first_contact(app):
    app.main_url()
    app.session.login(user="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()