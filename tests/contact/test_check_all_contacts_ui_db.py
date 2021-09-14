# -*- coding: utf-8 -*-
from model.contact import Contact
import re


def test_check_all_contacts_ui_db(app, db):
    if len(db.get_contact_list()) == 0:
        contact = Contact(
            firstname="firstname",
            lastname="lastname",
            nickname="nickname",
            company="test_company",
            home_phone="4444444",
            mobile_phone="0974472212",
            work_phone="5555555",
            fax="0969986635",
            secondary_phone="3244225",
            email_1="test1@example.com",
            email_2="test2@example.com",
            email_3="test3@example.com",
            address="Address"
        )
        app.contact.create(contact)
    db_list = db.get_contact_list()
    ui_list = app.contact.get_contact_list()
    assert sorted(db_list, key=Contact.id_or_max) == sorted(ui_list, key=Contact.id_or_max)
    for contact in ui_list:
        assert contact.firstname == db.get_contact_by_id(contact.id).firstname
        assert contact.lastname == db.get_contact_by_id(contact.id).lastname
        assert contact.address == db.get_contact_by_id(contact.id).address
        assert contact.all_emails == merge_emails(db.get_contact_by_id(contact.id))
        assert contact.all_phones == merge_phones(db.get_contact_by_id(contact.id))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email_1, contact.email_2, contact.email_3])))


def merge_phones(contact):
    def clear(s):
        return re.sub("[() -]", "", s)
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                        contact.secondary_phone]))))
