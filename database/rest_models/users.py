from db_util import DBResource

class Users(DBResource):

    TABLE = "Users"
    USERNAME = "username"
    PASSWORD = "password"

    def table_name(self):
        return self.TABLE

    def table_keys(self):
        return [self.USERNAME]

    def columns(self):
        return [(self.USERNAME, str), (self.PASSWORD, str)]
