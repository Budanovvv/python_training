from model.contact import Contact


def test_update_contact_first_phones(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name_frst="Petr"))
    app.contact.update_first_contact(Contact(name_frst="Petr_updated",
                                             home_ph="00000000",
                                             mobile_ph="00000000",
                                             work_ph="00000000",
                                             fax_ph="00000000"))
