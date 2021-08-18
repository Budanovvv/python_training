# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_delete_rnd_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Petr"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
