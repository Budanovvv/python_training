import re
from random import randrange


def test_check_phones_from_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_phones_from_home_page = app.contact.get_contact_list()[index].all_phones
    contact_phones_from_edit_page = merge_phones(app.contact.get_contact_from_edit_page(index))
    print("contact_phones_from_edit_page - " + str(contact_phones_from_edit_page))
    assert contact_phones_from_home_page == contact_phones_from_edit_page


def test_check_phones_from_view_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_phones_from_view_page = merge_phones(app.contact.get_contact_from_view_page(index))
    contact_phones_from_edit_page = merge_phones(app.contact.get_contact_from_edit_page(index))
    assert contact_phones_from_view_page == contact_phones_from_edit_page


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                        contact.secondary_phone]))))







