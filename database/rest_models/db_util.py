import os
import psycopg2
import psycopg2.extras
from flask_restful import Resource


class DBResource(Resource):

    def __init__(self, db_util):
        self.db_util = db_util
        return

    def append_where(self, parser_params, keys, sql_parts, sql_params_list):
        where_added = False
        for key in keys:
            if parser_params[key] != None:
                if not where_added:
                    sql_parts.append("WHERE {0}=%s".format(key))
                    where_added = True
                else:
                    sql_parts.append("AND {0}=%s".format(key))
                sql_params_list.append(parser_params[key])
        return sql_parts, sql_params_list


    def query(self, sql, sql_params=(), fetch=True):
        return self.db_util.query(sql, sql_params=sql_params, fetch=fetch)

class DBUtil(object):

    def __init__(self):
        self._init_conn()
        return

    def _init_conn(self):
        self.conn = psycopg2.connect(os.environ['POSTGRES_CONN_URI_CS316'])
        return

    def _rollback_and_close(self, cur):
        try:
            self.conn.rollback()
            cur.close()
            self.conn.close()
        except Exception as e:
            return

    def query(self, sql, sql_params=(), fetch=True):
        ret = None
        retries = 2
        for i in range(retries):
            cur = None
            try:
                cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                cur.execute(sql, sql_params)
                if fetch:
                    ret = cur.fetchall()
                self.conn.commit()
                cur.close()
                return True, ret
            except Exception as e:
                self._rollback_and_close(cur)
            self._init_conn()
            if i == retries-1:
                return False, e
