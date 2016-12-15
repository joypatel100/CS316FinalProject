from db_util import CustomDBResource, APIException
from flask_restful import reqparse
from nltk.metrics import jaccard_distance

def dis(data1, data2):
    a = set(data1.split())
    b = set(data2.split())
    ans=jaccard_distance(a,b)
    return ans

class Score(CustomDBResource):

    SPEECH_ID1 = "speech_id1"
    SPEECH_ID2 = "speech_id2"

    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument(self.SPEECH_ID1, required=True, type=int, location="args")
            parser.add_argument(self.SPEECH_ID2, required=True, type=int, location="args")
            params = parser.parse_args()
            sql = '''
                    SELECT Speech.speech_text
                    FROM Speech
                    WHERE Speech.speech_id=%s OR Speech.speech_id=%s
                '''
            sql_params = (params[self.SPEECH_ID1],params[self.SPEECH_ID2])
            suc, infos = self.query(sql, sql_params=sql_params, fetch=True)
            if len(infos) == 1:
                return {"score" : dis(infos[0][0], infos[0][0])}
            else:
                return {"score" : dis(infos[0][0], infos[1][0])}
        except Exception as e:
            return APIException(str(e)).ret_json()
