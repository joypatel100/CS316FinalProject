from bs4 import BeautifulSoup
from urllib import quote_plus
from urllib2 import urlopen, URLError
from datetime import datetime
import re
import psycopg2
import us
import json
import os
import config

#open database connection
conn = psycopg2.connect(dbname=config.dbname, user=config.user, port=config.port, password=config.password, host=config.host)
cur = conn.cursor()

#get members with their district
cur.execute("Select * from Speaker JOIN District ON Speaker.district_id=District.district_id where position_name='Senator';")
members = cur.fetchall()
conn.close()

already_scraped_member_ids = [400251, 400219, 400163, 400114, 400093, 400326, 400348, 400349, 400355, 400380, 400416, 400433, 400607, 412221, 412293]
for filename in os.listdir("C:\\Users\\Gautam\\OneDrive\\School\\CS316\\member_speeches"):
    if not filename.endswith('.py'):
        with open("C:\\Users\\Gautam\\OneDrive\\School\\CS316\\member_speeches\\" + filename) as data_file:
            data = json.load(data_file)
            if len(data) > 0:
                already_scraped_member_ids.append(data[0]['speaker_id'])

for member in members:
    print member[1]
    #get name and id of member
    lastname = ' '.join(member[1].split()[1:])
    id = member[0]
    #skip dummy entries and members already scraped
    if (id == 1 or id == 4 or id in already_scraped_member_ids):
        continue

    #get speeches of member from 2015-2016
    url = "https://www.congress.gov/advanced-search/command-line?query=crMemberRemarks:%22{0}%22&q={{%22cr-section%22:%22Senate%22,%22congress%22:%22114%22}}&pageSort=dateOfIntroduction:desc&pageSize=250".format(quote_plus(member[1]))

    # parse speech list
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "lxml") 
    speeches = soup.findAll("li", {"class": "compact"})

    #iterate over speeches
    output_speeches = []
    for item in speeches:
        #print " "
        try:
            document = urlopen(item.find("a")["href"]).read() # open speech
        except IOError as err:
            print("IO error: {0}".format(err))
            continue
        except URLError as err:
            print("URL error error: {0}".format(err))
            continue
        soup = BeautifulSoup(document, "lxml")
        date_object = datetime.strptime(soup.findAll("h3")[0].text, "%B %d, %Y ").date() # get speech date
        root = 'https://www.congress.gov/'
        speech_url = root + soup.find("li", {"class" : "fullTXT"}).find("a")["href"] # get link to raw speech text
        #print speech_url
        try:
            text = urlopen(speech_url).read() # open raw speech text
        except IOError as err:
            print("IO error: {0}".format(err))
            continue
        except URLError as err:
            print("URL error error: {0}".format(err))
            continue
        text = re.sub(r'[ ]{4,}.*\n', ' ', text) # strip indented text
        text = re.sub(r'\n', '', text) # strip newlines

        # split speech into speaker chunks
        # regex based off of: https://github.com/unitedstates/congressional-record/blob/master/congressionalrecord/fdsys/cr_parser.py
        chunks = re.split(r'(?:((?:Mr\.)|(?:Ms\.)|(?:Mrs\.)) ((?:[A-Z][a-z]{1,2})?[-A-Z\'\']{2,}(?: [-A-Z\'\']{2,})?)(?: of ([A-Z][a-z]+))?|(?:(Miss) ((?:[A-Z][a-z]{1,2})?[-A-Z\'\']{2,}(?: [-A-Z\'\']{2,})?)(?: of ([A-Z][a-z]+))?))', text)
        
        #iterate over speaker blocks
        for i in xrange(1, len(chunks), 7):
            speaker_title = chunks[i] if chunks[i] != None else chunks[i+3]
            speaker_lastname = chunks[i+1] if chunks[i+1] != None else chunks[i+4]
            speaker_state = chunks[i+2] if chunks[i+2] != None else chunks[i+5]
            speech = chunks[i+6]
            if len(speech) < 500: # don't deal with short speeches
                continue

            output_speech = {
                'speech_id': abs(hash(speech)) % (10 ** 9),
                'speech_text': speech,
                'date_said': str(date_object),
                'speaker_id': id,
                'username': 'master'
            };

            # if there is a state with the speaker attribution, make sure it matches the current member
            # in both cases, match member name
            if speaker_state is None:
                if lastname.lower() in speaker_lastname.lower():
                    output_speeches.append(output_speech)
                    #print output_speech
            else:
                if lastname.lower() in speaker_lastname.lower() and speaker_state.lower() == us.states.lookup(member[7]).name.lower():
                    output_speeches.append(output_speech)
                    #print output_speech
    with open(member[1].replace(' ', '') + '.json', 'w') as outfile:
        json.dump(output_speeches, outfile)