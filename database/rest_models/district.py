from flask_restful import Resource, reqparse
from db_util import DBResource

class District(DBResource):

    DISTICT_ID = "district_id"
    STATE = "state"
    NUM = "num"

    def _get_row_json(self, row):
        return {
            self.DISTICT_ID : row[0],
            self.STATE : row[1],
            self.NUM : row[2]
        }

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(self.DISTICT_ID, required=False, type=str, location="args")
        parser.add_argument(self.STATE, required=False, type=str, locations="args")
        parser.add_argument(self.NUM, required=False, type=int, location="args")
        parser_params = parser.parse_args()
        sql_params_list = []
        sql_parts = [
            """
            SELECT district_id, state, num
            FROM District
            """
        ]
        sql_parts, sql_params_list = self.append_where(parser_params,
            [self.DISTICT_ID, self.STATE, self.NUM], sql_parts, sql_params_list)
        sql = " ".join(sql_parts)
        sql_params = tuple(sql_params_list)
        suc, infos = self.query(sql, sql_params=sql_params)
        return {
            "data" : [self._get_row_json(info) for info in infos]
        }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(self.DISTICT_ID, required=True, type=str, location="json")
        parser.add_argument(self.STATE, required=True, type=str, locations="json")
        parser.add_argument(self.NUM, required=True, type=int, location="json")
        parser_params = parser.parse_args()
        sql = """
            INSERT INTO District(district_id, state, num)
            VALUES(%s, %s, %s)
            RETURNING district_id, state, num
        """
        sql_params = (parser_params[self.DISTICT_ID], parser_params[self.STATE], parser_params[self.NUM])
        suc, infos = self.query(sql, sql_params=sql_params)
        return self._get_row_json(infos[0])

    def put(self):
        return

    def delete(self):
        return
