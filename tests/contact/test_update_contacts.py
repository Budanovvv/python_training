from model.contact import Contact
from random import randrange
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_name(maxlen):
    symbols = string.ascii_letters + " " * 2
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.digits + "+" * 3 + " " * 3 + "(" * 3 + ")" * 3
    return "".join([random.choice(symbols) for i in range(maxlen)])


def random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@.example.com"


testdata = [Contact(firstname="",
                    middlename="",
                    lastname="",
                    nickname="",
                    company_title="",
                    company_name="",
                    address="",
                    home_phone="",
                    mobile_phone="",
                    work_phone="",
                    fax="",
                    email_1="",
                    email_2="",
                    email_3="",
                    home_page="",
                    birth_day="3",
                    birth_month="March",
                    birth_year="2000",
                    anniversary_day="4",
                    anniversary_month="February",
                    anniversary_year="2010",
                    secondary_address="",
                    secondary_phone="",
                    secondary_notes="")] + \
           [Contact(firstname=random_name(10),
                    middlename=random_name(10),
                    lastname=random_name(10),
                    nickname=random_name(10),
                    company_title=random_name(10),
                    company_name=random_name(10),
                    address=random_string("address ", 10),
                    home_phone=random_phone(10),
                    mobile_phone=random_phone(10),
                    work_phone=random_phone(10),
                    fax=random_phone(10),
                    email_1=random_email(10),
                    email_2=random_email(10),
                    email_3=random_email(10),
                    home_page="example.com",
                    birth_day="3",
                    birth_month="March",
                    birth_year="2000",
                    anniversary_day="4",
                    anniversary_month="February",
                    anniversary_year="2010",
                    secondary_address=random_string("secondary_address ", 10),
                    secondary_phone=random_phone(10),
                    secondary_notes="Secondary notes")
            for i in range(2)
            ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_update_rnd_contact_1(app, contact):
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


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_update_rnd_contact_2(app, contact):
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