CREATE TABLE IF NOT EXISTS SpeechAssociation
(speech_id1 INTEGER NOT NULL REFERENCES Speech(speech_id),
 speech_id2 INTEGER NOT NULL REFERENCES Speech(speech_id),
 score FLOAT NOT NULL CHECK(score <= 1 AND score >= 0),
 PRIMARY KEY (speech_id1, speech_id2)
);
