from db_util import DBResource

class SpeechAssociation(DBResource):

    TABLE = "SpeechAssociation"
    SPEECH_ID1 = "speech_id1"
    SPEECH_ID2 = "speech_id2"
    SCORE = "score"

    def table_name(self):
        return self.TABLE

    def table_keys(self):
        return [self.SPEECH_ID1, self.SPEECH_ID2]

    def columns(self):
        return [(self.SPEECH_ID1, int), (self.SPEECH_ID2, int), (self.SCORE, float)]
