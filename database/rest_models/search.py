from db_util import CustomDBResource, APIException
from flask_restful import reqparse

class Search(CustomDBResource):

    SPEECH_ID = "speech_id"
    SPEAKER = "speaker"
    KEY_WORDS = "keywords"
    SPEAKER_PARTY = "speaker_party"

    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument(self.SPEECH_ID, required=False, type=str, location="args")
            parser.add_argument(self.SPEAKER, required=False, type=str, location="args")
            parser.add_argument(self.KEY_WORDS, required=False, type=str, location="args")
            parser.add_argument(self.SPEAKER_PARTY, required=False, type=str, location="args")
            params = parser.parse_args()
            sql = '''
                    SELECT Speech.date_said, Speech.keywords, Speaker.name, Speaker.party_name
                    FROM Speech JOIN Speaker
                    ON Speech.speaker_id=Speaker.speaker_id
                '''
            infos = None
            if not params[self.SPEECH_ID] is None:
                suc, infos = self.query(sql + " WHERE Speech.speech_id=%s",
                    sql_params=(params[self.SPEECH_ID],),fetch=True)
            else:
                once = False
                sql_params = []
                if not params[self.SPEAKER] is None:
                    sql += " WHERE " if not once else " AND "
                    sql += "Speaker.name=%s"
                    once = True
                    sql_params.append(params[self.SPEAKER])
                if not params[self.KEY_WORDS] is None:
                    sql += " WHERE " if not once else " AND "
                    sql += "Speech.speech_text LIKE %s"
                    once = True
                    sql_params.append("%{0}%".format(params[self.KEY_WORDS]))
                if not params[self.SPEAKER_PARTY] is None:
                    sql += " WHERE " if not once else " AND "
                    sql += "Speaker.party_name=%s"
                    once = True
                    sql_params.append(params[self.SPEAKER_PARTY])
                print sql
                suc, infos = self.query(sql,sql_params=tuple(sql_params),fetch=True)
            keywords = lambda k : k[1:-1].replace("'","").replace('"',"").split(',')
            return {
                "data" :
                    [{
                        "date_said" : str(info[0]),
                        "keywords" : keywords(info[1]),
                        "speaker_name" : info[2],
                        "party_name" : info[3]
                    } for info in infos]
            }
        except Exception as e:
            return APIException(str(e)).ret_json()
