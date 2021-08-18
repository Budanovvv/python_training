from model.contact import Contact
from random import randrange


def test_update_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name_frst="Petr"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(name_frst="99999", name_lst="99999")
    contact.contact_id = old_contacts[index].contact_id
    app.contact.update_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    print("old_contacts-->>" + str(sorted(old_contacts, key=Contact.id_or_max)))
    print("new_contacts-->>" + str(sorted(old_contacts, key=Contact.id_or_max)))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)