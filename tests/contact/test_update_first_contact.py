from model.contact import Contact


def test_update_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name_frst="Petr"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name_frst="333", name_lst="3333")
    app.contact.update_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[0] = contact
    old_contacts[0].contact_id = new_contacts[0].contact_id
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)