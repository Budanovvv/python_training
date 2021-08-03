from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_link_text("add new").click()
        self.fill_form_contact_names(contact)
        self.fill_form_contact_company(contact)
        self.fill_form_contact_phones(contact)
        self.fill_contact_form_emails_hmpg(contact)
        self.fill_contact_form_annivers(contact)
        self.fill_contact_form_secondary(contact)
        # Submit contact creation
        wd.find_element_by_name("submit").click()
        # go back
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_name("selected[]")
        wd.find_element_by_link_text("home").click()

    def update_first_contact_phones(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_form_contact_phones(contact)
        # Submit contact creation
        wd.find_element_by_name("update").click()
        # go back
        wd.find_element_by_link_text("home page").click()

    def change_contact_value(self, field, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(value)

    def fill_form_contact_names(self, contact):
        self.change_contact_value("firstname", contact.name_frst)
        self.change_contact_value("middlename", contact.name_mdl)
        self.change_contact_value("lastname", contact.name_lst)
        self.change_contact_value("nickname", contact.name_nick)

    def fill_form_contact_company(self, contact):
        self.change_contact_value("title", contact.comp_title)
        self.change_contact_value("company", contact.comp_name)
        self.change_contact_value("address", contact.comp_addr)
        self.change_contact_value("address", contact.comp_addr)

    def fill_form_contact_phones(self, contact):
        self.change_contact_value("home", contact.home_ph)
        self.change_contact_value("mobile", contact.mobile_ph)
        self.change_contact_value("work", contact.work_ph)
        self.change_contact_value("fax", contact.fax_ph)

    def fill_contact_form_emails_hmpg(self, contact):
        self.change_contact_value("email", contact.email_1)
        self.change_contact_value("email2", contact.email_2)
        self.change_contact_value("email3", contact.email_3)
        self.change_contact_value("homepage", contact.home_page)

    def fill_contact_form_annivers(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.b_day)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.b_month)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.b_year)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.a_day)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.a_month)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.a_year)
        wd.find_element_by_name("new_group").click()

    def fill_contact_form_secondary(self, contact):
        self.change_contact_value("address2", contact.secondary_address)
        self.change_contact_value("phone2", contact.secondary_phone)
        self.change_contact_value("notes", contact.secondary_notes)