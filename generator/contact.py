# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"
# -n 10 -f data/contacts.json

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits\
              # + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(1, random.randrange(maxlen))])


def random_name(maxlen):
    symbols = string.ascii_letters + " " * 2
    return "".join([random.choice(symbols) for i in range(1, random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.digits
    return "+(" + "".join([random.choice(symbols) for i in range(maxlen)]) + ")" + \
           "".join([random.choice(symbols) for i in range(maxlen)]) + "-" + \
           "".join([random.choice(symbols) for i in range(maxlen)]) + "-" + \
           "".join([random.choice(symbols) for i in range(maxlen)])


def random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@example.com"


testdata = [Contact(firstname=random_name(10),
                    middlename=random_name(10),
                    lastname=random_name(10),
                    nickname=random_name(10),
                    company_title=random_name(10),
                    company_name=random_name(10),
                    address=random_string("address-", 10),
                    home_phone=random_phone(3),
                    mobile_phone=random_phone(3),
                    work_phone=random_phone(3),
                    fax=random_phone(3),
                    email_1=random_email(5),
                    email_2=random_email(5),
                    email_3=random_email(5),
                    home_page="example.com",
                    birth_day="3",
                    birth_month="March",
                    birth_year="2000",
                    anniversary_day="4",
                    anniversary_month="February",
                    anniversary_year="2010",
                    secondary_address=random_string("secondary_address ", 10),
                    secondary_phone=random_phone(3),
                    secondary_notes="Secondary notes")
            for i in range(5)
            ]

generate_contact_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(generate_contact_file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
