# -*- coding: utf-8 -*-
from selenium import webdriver
from contact import Contact
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        self.login(user="admin", password="secret")
        self.init_contact_creation()
        self.fill_contact_names(Contact(firstname="Some name",
                                        middlename="Some middle name",
                                        lastname="Some last name",
                                        nickname="Валентин"))
        self.fill_contact_title_compname_address()
        self.fill_contact_phones()
        self.fill_contact_emails()
        self.fill_contact_homepage()
        self.submit_new_contact()
        self.logout()

    def test_add_empty_contact(self):
        self.login(user="admin", password="secret")
        self.init_contact_creation()
        self.fill_contact_names(Contact(firstname="",
                                        middlename="",
                                        lastname="",
                                        nickname=""))
        self.fill_contact_title_compname_address()
        self.fill_contact_phones()
        self.fill_contact_emails()
        self.fill_contact_homepage()
        self.submit_new_contact()
        self.logout()

    def logout(self):
        wd = self.wd
        # logout
        wd.find_element_by_link_text("Logout").click()

    def submit_new_contact(self):
        wd = self.wd
        # Submit contact creation
        wd.find_element_by_name("submit").click()
        # Go to home page
        wd.find_element_by_link_text("home page").click()

    def fill_contact_homepage(self):
        wd = self.wd
        wd.find_element_by_name("homepage").send_keys("example.com")
        wd.find_element_by_name("theform").click()

    def fill_contact_emails(self):
        wd = self.wd
        # Fill in contact emails and homepage
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys("1111@example.com")
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").send_keys("22222@example.com")
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").send_keys("33333@example.com")
        wd.find_element_by_name("homepage").click()

    def fill_contact_phones(self):
        wd = self.wd
        # Fill in contact phones
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys("2345678")
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").send_keys("98765432")
        wd.find_element_by_name("work").send_keys("123456")
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").send_keys("234567")

    def fill_contact_title_compname_address(self):
        wd = self.wd
        # Fill in title, company name, address
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys("1111")
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").send_keys("BWR")
        wd.find_element_by_name("address").click()

    def fill_contact_names(self, contact):
        wd = self.wd
        # Fill in full name and nickname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

    def init_contact_creation(self):
        wd = self.wd
        # Init contact creation
        wd.find_element_by_link_text("add new").click()

    def login(self, user, password):
        wd = self.wd
        # Login
        wd.get("http://localhost/addressbook/edit.php")
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
