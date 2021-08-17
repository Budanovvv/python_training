from sys import maxsize


class Contact:

    def __init__(self, name_frst=None,
                 name_mdl=None,
                 name_lst=None,
                 name_nick=None,
                 comp_title=None,
                 comp_name=None,
                 comp_address=None,
                 home_ph=None,
                 mobile_ph=None,
                 work_ph=None,
                 fax_ph=None,
                 email_1=None,
                 email_2=None,
                 email_3=None,
                 home_page=None,
                 b_day=None,
                 b_month=None,
                 b_year=None,
                 a_day=None,
                 a_month=None,
                 a_year=None,
                 secondary_address=None,
                 secondary_phone=None,
                 secondary_notes=None,
                 contact_id=None):
        self.name_frst = name_frst
        self.name_mdl = name_mdl
        self.name_lst = name_lst
        self.name_nick = name_nick
        self.comp_title = comp_title
        self.comp_name = comp_name
        self.comp_address = comp_address
        self.home_ph = home_ph
        self.mobile_ph = mobile_ph
        self.work_ph = work_ph
        self.fax_ph = fax_ph
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.home_page = home_page
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year
        self.a_day = a_day
        self.a_month = a_month
        self.a_year = a_year
        self.secondary_address = secondary_address
        self.secondary_phone = secondary_phone
        self.secondary_notes = secondary_notes
        self.contact_id = contact_id

    def __repr__(self):
        return "%s, %s, %s" % (self.name_frst, self.name_lst, self.contact_id)

    def __eq__(self, other):
        return (self.contact_id is None
                or other.contact_id is None
                or self.contact_id == other.contact_id) \
               and (self.name_frst is None
                    or other.name_frst is None
                    or self.name_frst == other.name_frst) \
               and (self.name_lst is None
                    or other.name_lst is None
                    or self.name_lst == other.name_lst)

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize

