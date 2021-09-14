from model.contact import Contact
from random import randrange
import random


def test_update_rnd_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Petr"))
    old_contacts = db.get_contact_list()
    rnd_contact = random.choice(old_contacts)
    contact.id = rnd_contact.id
    app.contact.update_contact_by_id(rnd_contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(rnd_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
