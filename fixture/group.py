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

    def delete_first_group(self):
        wd = self.app.wd
        self.go_to_group_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        # Submit group deletion
        self.back_to_group_page()

    def update_first_group(self, new_group_data):
        wd = self.app.wd
        self.go_to_group_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_form_group(new_group_data)
        # Submit group update
        wd.find_element_by_name("update").click()
        self.back_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def go_to_group_page(self):
        wd = self.app.wd
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
        wd = self.app.wd
        self.change_group_value("group_name", group.name)
        self.change_group_value("group_header", group.header)
        self.change_group_value("group_footer", group.footer)



