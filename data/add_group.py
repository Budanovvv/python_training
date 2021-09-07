from model.group import Group
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits\
              # + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name - ", 10),
          header=random_string("header - ", 20),
          footer=random_string("footer - ", 20))
    for i in range(5)
]


# testdata = [
#     Group(name=name, header=header, footer=header)
#     for name in ["", random_string("name ", 10)]
#     for header in ["", random_string("header ", 20)]
#     for footer in ["", random_string("footer ", 20)]
# ]

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]