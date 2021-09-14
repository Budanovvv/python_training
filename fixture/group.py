from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.go_to_group_page()
        wd.find_element_by_name("new").click()
        self.fill_form_group(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.back_to_group_page()
        self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_all_groups(self):
        wd = self.app.wd
        self.go_to_group_page()
        for i in range(len(wd.find_elements_by_name("selected[]"))):
            wd.find_elements_by_name("selected[]")[i].click()

    def test_delete_all_groups(self):
        self.select_all_groups()
        self.delete_groups()

    def delete_group_by_index(self, index):
        self.go_to_group_page()
        self.select_group_by_index(index)
        self.delete_groups()
        self.group_cache = None

    def delete_group_by_id(self, id):
        self.go_to_group_page()
        self.select_group_by_id(id)
        self.delete_groups()
        self.group_cache = None

    def delete_groups(self):
        wd = self.app.wd
        wd.find_element_by_name("delete").click()
        self.back_to_group_page()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def update_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.go_to_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_form_group(new_group_data)
        # Submit group update
        wd.find_element_by_name("update").click()
        self.back_to_group_page()
        self.group_cache = None

    def update_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.go_to_group_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("edit").click()
        self.fill_form_group(new_group_data)
        # Submit group update
        wd.find_element_by_name("update").click()
        self.back_to_group_page()
        self.group_cache = None

    def update_first_group(self, new_group_data):
        self.update_group_by_index(0, new_group_data)

    def select_first_group(self):
        self.select_group_by_index(0)

    def go_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and
                len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def back_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def change_group_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_form_group(self, group):
        self.change_group_value("group_name", group.name)
        self.change_group_value("group_header", group.header)
        self.change_group_value("group_footer", group.footer)

    def count(self):
        wd = self.app.wd
        self.go_to_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.go_to_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                group_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=group_id))
        return list(self.group_cache)
