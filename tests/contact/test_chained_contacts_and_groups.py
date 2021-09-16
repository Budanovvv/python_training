import random
from model.contact import Contact
from model.group import Group


def test_check_add_contact_to_the_group(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Petr"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="First"))
    group = random.choice(orm.get_group_list())
    group_id = group.id
    contact = random.choice(orm.get_contacts_not_in_group(group))
    contact_id = contact.id
    app.contact.add_contact_to_the_group(contact_id, group_id)
    assert db.get_contact_by_id(contact_id) in orm.get_contacts_in_group(Group(id=group_id))


def test_check_delete_contact_from_the_group(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Petr"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="First"))
    contact = random.choice(orm.get_contact_list())
    contact_id = contact.id
    group = random.choice(orm.get_group_list())
    group_id = group.id
    if contact not in orm.get_contacts_in_group(group):
        app.contact.add_contact_to_the_group(contact_id, group_id)
    app.contact.del_contact_from_the_group(contact_id, group_id)
    assert db.get_contact_by_id(contact_id) not in orm.get_contacts_in_group(Group(id=group_id))
