from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, group_id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.group_id = group_id

    def __repr__(self):
        return "%s, %s" % (self.group_id, self.name)

    def __eq__(self, other):
        return (self.group_id is None
                or other.group_id is None
                or self.group_id == other.group_id) and self.name == other.name

    def id_or_max(self):
        if self.group_id:
            return int(self.group_id)
        else:
            return maxsize