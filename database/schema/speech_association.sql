CREATE TABLE IF NOT EXISTS speech_association
(speech_id1 INTEGER NOT NULL REFERENCES Speech(speech_id),
   speech_id2 INTEGER NOT NULL REFERENCES Speech(speech_id),
   score FLOAT NOT NULL CHECK(score <= 1 AND score >= 0),
   name1 VARCHAR(256) REFERENCES Speaker(name),
   name2 VARCHAR(256) REFERENCES Speaker(name),
   PRIMARY KEY (speech_id1, speech_id2)
);
