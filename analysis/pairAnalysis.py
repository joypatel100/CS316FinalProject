import psycopg2
from nltk.metrics import jaccard_distance

conn = psycopg2.connect(dbname='CS316FinalProjectDB', user='postgres', port=5432, password='abcde12345', host='104.196.202.43')
cur = conn.cursor()
cur.execute("SELECT speech_id,speech_text,speaker_id,wordcount FROM Speech;")
speeches = cur.fetchall()

#distance matrix --jaccard distance
def dis(data1, data2):
        a = set(data1.split())
        b = set(data2.split())
        ans=jaccard_distance(a,b)
        return ans

#find the longest speech for each speaker
text={}
wordcount={}
longest={}
for (speechid,speech,speaker,word) in speeches:
        text[speechid]=speech
        if speaker not in wordcount:
                wordcount[speaker]=word
                longest[speaker]=speechid
        elif wordcount[speaker] < word:
                wordcount[speaker]=word
                longest[speaker]=speechid

cur2=conn.cursor()
for id1 in longest.itervalues():
    t1=text[id1]
    for id2 in longest.itervalues():
        t2=text[id2]
        score=dis(t1,t2)
        cur2.execute("INSERT INTO Speech_association SELECT %s,%s,%s WHERE NOT EXISTS (SELECT * FROM Speech_association WHERE speech_id1=%s AND speech_id2=%s)",(id1,id2,score,id1,id2))
        conn.commit()

cur2.close()
cur.close()
conn.close()
