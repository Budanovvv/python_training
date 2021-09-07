from model.contact import Contact
from random import randrange
import pytest


def test_update_rnd_contact_1(app, json_contacts):
    contact = json_contacts
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Petr"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
# def test_update_rnd_contact_2(app, contact):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Petr"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact.id = old_contacts[index].id
#     app.contact.update_contact_by_index(contact, index)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == app.contact.count()
#     old_contacts[index] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
