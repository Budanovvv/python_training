import pymysql
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname, middlename, nickname, title, "
                           "company, address FROM addressbook WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, middlename, nickname, title, company, address) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, middlename=middlename,
                                    nickname=nickname, title=title, company=company, address=address))
        finally:
            cursor.close()
        return list

    def get_contact_by_id(self, id_in):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname, middlename, nickname, company, "
                           "title, address, email, email2, email3, home, mobile, work, phone2 "
                           "FROM addressbook WHERE deprecated='0000-00-00 00:00:00' and id='%s'" % id_in)
            (id, firstname, lastname, middlename, nickname, company, title,
             address, email, email2, email3, home, mobile, work, phone2) = cursor.fetchone()
            contact_return = Contact(id=str(id), firstname=firstname, lastname=lastname, middlename=middlename,
                                     nickname=nickname, company=company, title=title, address=address, email_1=email,
                                     email_2=email2, email_3=email3, home_phone=home, mobile_phone=mobile, work_phone=work,
                                     secondary_phone=phone2)
        finally:
            cursor.close()
        return contact_return
