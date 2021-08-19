from model.contact import Contact
from random import randrange


def test_update_rnd_contact_1(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Petr"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="99999", lastname="99999")
    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_update_rnd_contact_2(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Petr"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="99999", lastname="99999")
    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)