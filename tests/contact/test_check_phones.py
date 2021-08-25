import re
from random import randrange


def test_check_phones_from_home_page(app):
    contact_list_len = len(app.contact.get_contact_list())
    index = randrange(contact_list_len)
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_home_page.home_phone == clear(contact_from_edit_page.home_phone)
    assert contact_from_home_page.work_phone == clear(contact_from_edit_page.work_phone)
    assert contact_from_home_page.mobile_phone == clear(contact_from_edit_page.mobile_phone)
    assert contact_from_home_page.secondary_phone == clear(contact_from_edit_page.secondary_phone)


def test_check_phones_from_view_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone


def clear(s):
    return re.sub("[() -]", "", s)






