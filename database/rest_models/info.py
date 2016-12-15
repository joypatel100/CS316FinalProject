from db_util import CustomDBResource, APIException
from flask_restful import reqparse

class Info(CustomDBResource):

    SPEECH_ID = "speech_id"

    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument(self.SPEECH_ID, required=True, type=str, location="args")
            params = parser.parse_args()
            sql = '''
                    SELECT Speech.speech_text, Speech.date_said, Speech.keywords,
                    Speech.sentiment, Speaker.name, Speaker.party_name
                    FROM Speech JOIN Speaker
                    ON Speech.speaker_id=Speaker.speaker_id
                    WHERE Speech.speech_id=%s
                '''
            sql_params = (params[self.SPEECH_ID],)
            suc, infos = self.query(sql, sql_params=sql_params, fetch=True)
            info = infos[0]
            keywords = info[2][1:-1]
            keywords = keywords.replace("'","")
            keywords = keywords.replace('"',"")
            keywords = keywords.split(',')
            ret = {
                "speech_text" : info[0],
                "date_said" : str(info[1]),
                "keywords" : keywords,
                "sentiment" : info[3],
                "speaker_name" : info[4],
                "party_name" : info[5]
            }
            return ret
        except Exception as e:
            return APIException(str(e)).ret_json()
