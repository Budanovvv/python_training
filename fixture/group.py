class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        # Go to group page
        wd.find_element_by_name("new").click()
        # Fill group
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        # go back
        wd.find_element_by_link_text("group page").click()

    def delete(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        # Go to group page
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        # Submit group deletion
        wd.find_element_by_link_text("group page").click()
        # go back

    def update(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        # Go to group page
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        # Change group
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Update group
        wd.find_element_by_name("update").click()
        # go back
        wd.find_element_by_link_text("group page").click()



