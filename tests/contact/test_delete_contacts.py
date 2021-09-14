# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_delete_rnd_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Petr"))
    old_contacts = db.get_contact_list()
    rnd_contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(rnd_contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(rnd_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
