from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_form_contact(contact)
        # Submit contact creation
        wd.find_element_by_name("submit").click()
        # go back
        self.go_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_name("selected[]")
        self.go_to_home_page()

    def update_first_contact(self, contact):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_form_contact(contact)
        # Submit contact creation
        wd.find_element_by_name("update").click()
        self.go_to_home_page()

    def go_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and
                len(wd.find_elements_by_xpath("//input[@value='Delete']")) > 0):
            wd.find_element_by_link_text("home").click()

    def change_contact_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_form_contact(self, contact):
        self.change_contact_value("firstname", contact.name_frst)
        self.change_contact_value("middlename", contact.name_mdl)
        self.change_contact_value("lastname", contact.name_lst)
        self.change_contact_value("nickname", contact.name_nick)
        self.change_contact_value("title", contact.comp_title)
        self.change_contact_value("company", contact.comp_name)
        self.change_contact_value("address", contact.comp_address)
        self.change_contact_value("address", contact.comp_address)
        self.change_contact_value("home", contact.home_ph)
        self.change_contact_value("mobile", contact.mobile_ph)
        self.change_contact_value("work", contact.work_ph)
        self.change_contact_value("fax", contact.fax_ph)
        self.change_contact_value("email", contact.email_1)
        self.change_contact_value("email2", contact.email_2)
        self.change_contact_value("email3", contact.email_3)
        self.change_contact_value("homepage", contact.home_page)
        self.change_contact_value("address2", contact.secondary_address)
        self.change_contact_value("phone2", contact.secondary_phone)
        self.change_contact_value("notes", contact.secondary_notes)

    def fill_contact_form_anniversary(self, contact):
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

    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))