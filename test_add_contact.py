# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(user="admin", password="secret")
    app.fill_contact(Contact(name_frst="Petr",
                              name_mdl="Petrovych",
                              name_lst="Petrov",
                              name_nick="PetrCompNick",
                              comp_title="PetrComp_1111",
                              comp_name="PetrComp",
                              comp_addr="Ulica 2",
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

    app.logout()
