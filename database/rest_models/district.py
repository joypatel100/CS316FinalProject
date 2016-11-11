from flask_restful import Resource, reqparse
from db_util import DBResource

class District(DBResource):

    TABLE = "District"
    DISTICT_ID = "district_id"
    STATE = "state"
    NUM = "num"

    def table_name(self):
        return self.TABLE

    def table_keys(self):
        return [self.DISTICT_ID]

    def columns(self):
        return [(self.DISTICT_ID, int), (self.STATE, str), (self.NUM, int)]
