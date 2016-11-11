import govtrack
from govtrack.api import GovTrackClient
client = GovTrackClient()
roles = client.role({"current": "true", "limit": "600"})
from datetime import datetime

conn = psycopg2.connect(dbname='CS316FinalProjectDB', user='postgres', port=5432, password='abcde12345', host='104.196.18.176')
cur = conn.cursor()
for obj in roles['objects']:
    person = obj['person']
    id = int(person['id'])
    name = person['firstname'] + ' ' + person['lastname']
    dob = datetime.strptime(person['birthday'], "%Y-%m-%d").date()
    party_name = obj['party']
    position_name = obj['role_type_label']
    district = obj['district'] if obj['district'] is not None else 0
    dist_id = hash(obj['state'] + str(district)) % 1000000000
    if dist_id not in ids:
        cur.execute("""INSERT into District VALUES (%s, %s, %s);""", (dist_id, obj['state'], district))
        ids.append(dist_id)
    cur.execute("""INSERT into Speaker VALUES (%s, %s, %s, %s, %s, %s);""", (id, name, dob, party_name, position_name, dist_id))

cur.execute("Select * from Speaker;")
speakers = cur.fetchall()
speakers
conn.commit()
conn.close()
