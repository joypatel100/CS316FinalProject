import os
import psycopg2
import psycopg2.extras
from flask_restful import Resource, reqparse
import datetime

'''
Interface
class DBResource(Resouce):

    def table_name():
        pass

    def table_keys():
        pass

    def columns(self):
        pass

'''

class DBResource(Resource):

    def __init__(self, *arg):
        self.db_util = arg[0]
        return

    def table_name():
        pass

    def table_keys():
        pass

    def columns(self):
        pass

    def _generate_parser_params(self, variables):
        parser = reqparse.RequestParser()
        names = []
        for (name, t, req, loc) in variables:
            parser.add_argument(name, required=req, type=t, location=loc)
            names.append(name)
        return parser.parse_args(), names

    def _column_names(self):
        return [name for name, t in self.columns()]

    def _json(self, row):
        ret = {}
        cols = self.columns()
        for i in range(len(row)):
            ret[cols[i][0]] = str(row[i]) if isinstance(row[i], datetime.date) else row[i]
        return ret

    def _get_vars(self):
        return [(name, t, False, "args") for name, t in self.columns()]

    def get(self):
        table, variables = self.table_name(), self._get_vars()
        parser_params, names = self._generate_parser_params(variables)
        sql_params_list = []
        sql_parts = ["""
            SELECT {0} FROM {1}
        """.format(", ".join(names), table)]
        sql_parts, sql_params_list = self.append_where(parser_params, names, sql_parts, sql_params_list)
        sql = " ".join(sql_parts)
        sql_params = tuple(sql_params_list)
        suc, infos = self.query(sql, sql_params=sql_params)
        if not suc:
            return {"error" : infos.message}
        return {
            "data" : [self._json(info) for info in infos]
        }

    def _post_vars(self):
        return [(name, t, True, "json") for name, t in self.columns()]

    def post(self):
        table, variables = self.table_name(), self._post_vars()
        parser_params, names = self._generate_parser_params(variables)
        sql = """
            INSERT INTO {0}({1})
            VALUES({2})
            RETURNING {3}
        """.format(table, ", ".join(names), ", ".join(["%s" for i in names]), ", ".join(self._column_names()))
        sql_params = tuple([parser_params[name] for name in names])
        suc, infos = self.query(sql, sql_params=sql_params)
        if not suc:
            return {"error" : infos.message}
        return self._json(infos[0])

    def _put_vars(self):
        cols = self.columns()
        ret = []
        table_keys = self.table_keys()
        for name, t in cols:
            if name in table_keys:
                ret.append((name, t, True, "json"))
            else:
                ret.append((name, t, False, "json"))
        return ret

    def put(self):
        table = self.table_name()
        table_keys = self.table_keys()
        variables = self._put_vars()
        parser_params, names = self._generate_parser_params(variables)
        keys = [key for key in parser_params if parser_params[key]!=None]
        print parser_params
        if len(keys) == 0:
            return {"message" : "no change"}
        sql_parts = ["""
            UPDATE {0} SET {1}
        """.format(table, ", ".join(["{0}=%s".format(key) for key in keys]))]
        sql_params_list = [parser_params[key] for key in keys]
        sql_parts, sql_params_list = self.append_where(parser_params, table_keys, sql_parts, sql_params_list)
        sql_parts.append(" RETURNING {0}".format(", ".join(self._column_names())))
        sql_params = tuple(sql_params_list)
        sql = " ".join(sql_parts)
        suc, infos = self.query(sql, sql_params=sql_params)
        if not suc:
            return {"error" : infos.message}
        return self._json(infos[0])

    def _delete_vars(self):
        cols = self.columns()
        table_keys = self.table_keys()
        return [(name, t, True, "args") for name, t in cols if name in table_keys]

    def delete(self):
        table, variables = self.table_name(), self._delete_vars()
        parser_params, names = self._generate_parser_params(variables)
        keys = [key for key in parser_params if parser_params[key]!=None]
        if len(keys) == 0:
            return {"message" : "no change"}
        sql_parts = ["""
            DELETE FROM {0}
        """.format(table)]
        sql_params_list = []
        sql_parts, sql_params_list = self.append_where(parser_params, names, sql_parts, sql_params_list)
        sql_parts.append(" RETURNING {0}".format(", ".join(self._column_names())))
        sql = " ".join(sql_parts)
        sql_params = tuple(sql_params_list)
        print sql, sql_params
        suc, infos = self.query(sql, sql_params=sql_params)
        if not suc:
            return {"error" : infos.message}
        return self._json(infos[0])



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
