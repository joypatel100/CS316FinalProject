import json
import os
import requests
import config

senate_directory = "C:\\Users\\Gautam\\OneDrive\\School\\CS316\\senate_speeches\\"
house_directory = "C:\\Users\\Gautam\\OneDrive\\School\\CS316\\house_speeches\\"

directories = [house_directory]

with open("uploaded.txt", "a+") as outfile:
    uploaded_files = outfile.read().splitlines()
    outfile.seek(0)
    for directory in directories:
        for filename in os.listdir(directory):
            if filename in uploaded_files:
                continue
            with open(directory + filename) as data_file:
                data = json.load(data_file)
                errors = False
                success=False
                for speech in data:
                    r = requests.post(config.resturl + '/speech', json=speech)
                    if r.status_code != requests.codes.ok or len(data) == 0:
                        errors=True
                        print "error: status={0}, data={1}".format(r.status_code, data)
                    else:
                        print ("{0} {1}".format(filename, speech['speech_id']))
                        success=True
                if success:
                    try:
                        outfile.write(filename + "\n")
                    except IOError as e:
                        print e.message
                      