CREATE TABLE IF NOT EXISTS Speaker
(speaker_id INTEGER PRIMARY KEY NOT NULL,
 name VARCHAR(256) NOT NULL,
 dob date NOT NULL,
 party_name VARCHAR(256) NOT NULL,
 position_name VARCHAR(256) NOT NULL REFERENCES Position(position_name),
 district_id INTEGER REFERENCES District(district_id)
);
