import random
from model.contact import Contact
from model.group import Group


def test_check_add_contact_to_the_group(app, orm, db):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Petr"))
    contact = random.choice(orm.get_contact_list())
    contact_id = contact.id
    group = random.choice(orm.get_group_list())
    group_id = group.id
    app.contact.add_contact_to_the_group(contact_id, group_id)
    assert db.get_contact_by_id(contact_id) in orm.get_contacts_in_group(Group(id=group_id))




