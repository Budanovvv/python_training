import re
from random import randrange


def test_check_contact_from_edit_page(app):
    contact_list_len = len(app.contact.get_contact_list())
    index = randrange(contact_list_len)
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_home_page.all_phones == merge_phones(contact_from_edit_page)
    assert contact_from_home_page.all_emails == merge_emails(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                        contact.secondary_phone]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email_1, contact.email_2, contact.email_3])))
