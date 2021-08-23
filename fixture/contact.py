from selenium.webdriver.support.ui import Select
from model.contact import Contact


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
        self.contact_cache = None

    def update_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_form_contact(contact)
        # Submit contact creation
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self, index):
        self.delete_contact_by_index(0)

    def update_first_contact(self, contact, index):
        self.update_contact_by_index(contact, index)

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
        self.change_contact_value("firstname", contact.firstname)
        self.change_contact_value("middlename", contact.middlename)
        self.change_contact_value("lastname", contact.lastname)
        self.change_contact_value("nickname", contact.nickname)
        self.change_contact_value("title", contact.company_title)
        self.change_contact_value("company", contact.company_name)
        self.change_contact_value("address", contact.company_address)
        self.change_contact_value("address", contact.company_address)
        self.change_contact_value("home", contact.home_phone)
        self.change_contact_value("mobile", contact.mobile_phone)
        self.change_contact_value("work", contact.work_phone)
        self.change_contact_value("fax", contact.fax)
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
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("new_group").click()

    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                contact_id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=contact_id))
        return list(self.contact_cache)
