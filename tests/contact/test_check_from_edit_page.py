import re
from random import randrange


def test_check_contact_from_edit_page(app):
    contact_list_len = len(app.contact.get_contact_list())
    index = randrange(contact_list_len)
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_home_page.home_phone == clear(contact_from_edit_page.home_phone)
    assert contact_from_home_page.work_phone == clear(contact_from_edit_page.work_phone)
    assert contact_from_home_page.mobile_phone == clear(contact_from_edit_page.mobile_phone)
    assert contact_from_home_page.secondary_phone == clear(contact_from_edit_page.secondary_phone)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.email_1 == contact_from_edit_page.email_1
    assert contact_from_home_page.email_2 == contact_from_edit_page.email_2
    assert contact_from_home_page.email_3 == contact_from_edit_page.email_3


def clear(s):
    return re.sub("[() -]", "", s)