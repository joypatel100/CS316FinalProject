from db_util import DBResource

class Speaker(DBResource):

    TABLE = "Speaker"
    SPEAKER_ID = "speaker_id"
    NAME = "name"
    DOB = "dob"
    PARTY_NAME = "party_name"
    POSITION_NAME = "position_name"
    DISTICT_ID = "district_id"

    def table_name(self):
        return self.TABLE

    def table_keys(self):
        return [self.SPEAKER_ID]

    def columns(self):
        return [(self.SPEAKER_ID, int), (self.NAME, str), (self.DOB, str),
                (self.PARTY_NAME, str), (self.POSITION_NAME, str),
                (self.DISTICT_ID, int)]
