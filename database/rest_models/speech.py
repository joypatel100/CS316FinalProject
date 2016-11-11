from db_util import DBResource

class Speech(DBResource):

    TABLE = "Speech"
    SPEECH_ID = "speech_id"
    SPEECH_TEXT = "speech_text"
    DATE_SAID = "date_said"
    SPEAKER_ID = "speaker_id"
    USERNAME = "username"

    def table_name(self):
        return self.TABLE

    def table_keys(self):
        return [self.SPEECH_ID]

    def columns(self):
        return [(self.SPEECH_ID, int), (self.SPEECH_TEXT, str), (self.DATE_SAID, str),
                (self.SPEAKER_ID, int), (self.USERNAME, str)]
