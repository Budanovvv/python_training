from model.contact import Contact


def test_update_contact_first_phones(app):
    app.main_url()
    app.session.login(user="admin", password="secret")
    app.contact.update_first_contact_phones(Contact(home_ph="00000000",
                                             mobile_ph="00000000",
                                             work_ph="00000000"))
    # Один номер пропустил специально - проверить корректность работы
    app.session.logout()
