from model.contact import Contact


def test_update_contact_first_phones(app):
    app.contact.update_first_contact(Contact(name_frst="Petr_updated",
                                             home_ph="00000000",
                                             mobile_ph="00000000",
                                             work_ph="00000000",
                                             fax_ph="00000000"))
