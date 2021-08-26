from sys import maxsize


class Contact:

    def __init__(self, firstname=None,
                 middlename=None,
                 lastname=None,
                 nickname=None,
                 company_title=None,
                 company_name=None,
                 address=None,
                 home_phone=None,
                 mobile_phone=None,
                 work_phone=None,
                 fax=None,
                 email_1=None,
                 email_2=None,
                 email_3=None,
                 home_page=None,
                 birth_day=None,
                 birth_month=None,
                 birth_year=None,
                 anniversary_day=None,
                 anniversary_month=None,
                 anniversary_year=None,
                 secondary_address=None,
                 secondary_phone=None,
                 secondary_notes=None,
                 all_phones=None,
                 all_emails=None,
                 id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company_title = company_title
        self.company_name = company_name
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.home_page = home_page
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.secondary_address = secondary_address
        self.secondary_phone = secondary_phone
        self.secondary_notes = secondary_notes
        self.all_phones = all_phones
        self.all_emails = all_emails
        self.id = id

    def __repr__(self):
        return "%s, %s, %s, %s, %s" % (self.firstname, self.lastname, self.id, self.all_phones, self.all_emails)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
