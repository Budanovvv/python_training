from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_list()
        wd.find_element_by_link_text("add new").click()
        self.fill_form_contact(contact)
        # Submit contact creation
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def update_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_contact_list()
        self.open_contact_edit_by_index(index)
        self.fill_form_contact(contact)
        # Submit contact creation
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def update_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_list()
        self.open_contact_edit_by_id(id)
        self.fill_form_contact(contact)
        # Submit contact creation
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_contact_edit_by_id(self, id):
        self.open_contact_list()
        row = self.find_checkbox_by_id(id)
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def find_checkbox_by_id(self, id_contact):
        wd = self.app.wd
        return wd.find_element_by_css_selector("input[value='%s']" % id_contact)

    def open_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_list()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_list()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, secondary_phone=secondary_phone)

    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        home_phone = wd.find_element_by_name('home').get_attribute('value')
        work_phone = wd.find_element_by_name('work').get_attribute('value')
        mobile_phone = wd.find_element_by_name('mobile').get_attribute('value')
        secondary_phone = wd.find_element_by_name('phone2').get_attribute('value')
        email_1 = wd.find_element_by_name('email').get_attribute('value')
        email_2 = wd.find_element_by_name('email2').get_attribute('value')
        email_3 = wd.find_element_by_name('email3').get_attribute('value')
        address = wd.find_element_by_name('address').text
        return Contact(firstname=firstname, lastname=lastname, id=id, home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, secondary_phone=secondary_phone, email_1=email_1, email_2=email_2,
                       email_3=email_3, address=address)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_list()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_list()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def update_first_contact(self, contact, index):
        self.update_contact_by_index(contact, index)

    def open_contact_list(self):
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
        self.change_contact_value("address", contact.address)
        self.change_contact_value("address", contact.address)
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
        self.open_contact_list()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_list()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_emails=all_emails, all_phones=all_phones, address=address))
        return list(self.contact_cache)

    def add_contact_to_the_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contact_list()
        self.find_checkbox_by_id(contact_id).click()
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_value(group_id)
        wd.find_element_by_name("add").click()



