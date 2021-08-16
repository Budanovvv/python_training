# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    # old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(name_frst="Petr",
                               name_mdl="Petrovych",
                               name_lst="Petrov",
                               name_nick="PetrCompNick",
                               comp_title="PetrComp_1111",
                               comp_name="PetrComp",
                               comp_address="Ulica 2",
                               home_ph="111-111-111",
                               mobile_ph="222-222-222",
                               work_ph="333-333-333",
                               fax_ph="444-444-444",
                               email_1="111111@example.com",
                               email_2="222222@example.com",
                               email_3="333333@example.com",
                               home_page="example.com",
                               b_day="3",
                               b_month="March",
                               b_year="2000",
                               a_day="4",
                               a_month="February",
                               a_year="2010",
                               secondary_address="Secondary Address unknown",
                               secondary_phone="Secondary phone ?",
                               secondary_notes="Secondary notes"))
    # new_contacts = app.group.get_group_list()
    # assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    # old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(name_frst="Empty",
                               b_day="1",
                               b_month="March",
                               b_year="",
                               a_day="1",
                               a_month="March",
                               a_year="",
                               secondary_notes="Really empty"))
    # new_contacts = app.group.get_group_list()
    # assert len(old_contacts) + 1 == len(new_contacts)
