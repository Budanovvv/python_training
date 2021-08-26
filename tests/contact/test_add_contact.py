# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    print("old_contacts - " + str(old_contacts[0]))
    contact = Contact(firstname="Petr",
                      middlename="Petrovych",
                      lastname="Petrov",
                      nickname="PetrCompNick",
                      company_title="PetrComp_1111",
                      company_name="PetrComp",
                      address="Ulica 2",
                      home_phone="111-111-111",
                      mobile_phone="222-222-222",
                      work_phone="333-333-333",
                      fax="444-444-444",
                      email_1="111111@example.com",
                      email_2="222222@example.com",
                      email_3="333333@example.com",
                      home_page="example.com",
                      birth_day="3",
                      birth_month="March",
                      birth_year="2000",
                      anniversary_day="4",
                      anniversary_month="February",
                      anniversary_year="2010",
                      secondary_address="Secondary Address unknown",
                      secondary_phone="Secondary phone ?",
                      secondary_notes="Secondary notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Empty",
                      birth_day="1",
                      birth_month="March",
                      birth_year="",
                      anniversary_day="1",
                      anniversary_month="March",
                      anniversary_year="",
                      secondary_notes="Really empty")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

