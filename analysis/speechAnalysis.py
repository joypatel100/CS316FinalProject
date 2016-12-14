import psycopg2
from textblob import TextBlob
from collections import Counter

conn = psycopg2.connect(dbname='CS316FinalProjectDB', user='postgres', port=5432, password='abcde12345', host='104.196.202.43')
cur = conn.cursor()
cur.execute("SELECT speech_id,speech_text FROM Speech;")
speech = cur.fetchall()

# get keyword
def Top3_Common(tb):
	lst=tb.noun_phrases
    data = Counter(lst)
    wordcount=data.most_common(3)
    ans=[]
    for i in wordcount:
    	ans.append(i[0])
    return ans


id=[]
count=[]
keyword=[]
polarity=[]
subjectivity=[]
for (t1,t2) in speech:
        id.append(t1)
        count.append(len(t2.split()))
        text=TextBlob(t2)
        keyword.append(Top3_Common(text))
        polarity.append(text.sentiment.polarity)
        subjectivity.append(text.sentiment.subjectivity)


for i in range(len(id)):
	cur2=conn.cursor()
	cur2.execute("UPDATE Speech SET wordcount = %s WHERE speech_id = %s",(count[i],id[i]))
	conn.commit()
	cur2.execute("UPDATE Speech SET keywords = %s WHERE speech_id = %s",(keyword[i],id[i]))
	conn.commit()
	cur2.execute("UPDATE Speech SET polarity = %s WHERE speech_id = %s",(polarity[i],id[i]))
	conn.commit()
	cur2.execute("UPDATE Speech SET subjectivity = %s WHERE speech_id = %s",(subjectivity[i],id[i]))
	conn.commit()
	cur2.close()

cur.close()
conn.close()
