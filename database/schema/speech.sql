CREATE TABLE IF NOT EXISTS Speech
(speech_id INTEGER PRIMARY KEY NOT NULL,
 speech_text VARCHAR(100000) NOT NULL,
 date_said date NOT NULL,
 speaker_id INTEGER NOT NULL REFERENCES Speaker(speaker_id),
 username VARCHAR(256) NOT NULL REFERENCES Users(username),
 wordcount INTEGER,
 keywords TEXT,
 sentiment DOUBLE PRECISION,
 subjectivity DOUBLE PRECISION
);
