from db_util import DBResource

class Position(DBResource):

    TABLE = "Position"
    POSITION_NAME = "position_name"
    TERM = "term"
    SCOPE = "scope"

    def table_name(self):
        return self.TABLE

    def table_keys(self):
        return [self.POSITION_NAME]

    def columns(self):
        return [(self.POSITION_NAME, str), (self.TERM, int), (self.SCOPE, str)]
