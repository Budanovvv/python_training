from model.contact import Contact


def test_add_contact(app):
    app.home_page()
    app.session.login(user="admin", password="secret")
    app.contact.update_first_contact(Contact(name_frst="Petr_updated",
                                             home_ph="00000000",
                                             mobile_ph="00000000",
                                             work_ph="00000000",
                                             fax_ph="00000000"))
    app.session.logout()
