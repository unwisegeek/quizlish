#!/usr/bin/python

# Small script to take two inputs and feed them to an IFTTT event named quizlish_answers
# By John Madon for the Quizlish Project

import os
import sys
import subprocess

key = ""
url = ""
event_id = "quizlish_answers"

if os.path.exists('./key'):
    key = open('./key', 'r').read()

url = "https://maker.ifttt.com/trigger/{}/with/key/{}".format(event_id, key).strip('\r').strip('\n')

if len(sys.argv) == 3 and len(key) > 0:
   arg1 = sys.argv[1]
   arg2 = sys.argv[2]
   data = '{{"value1":"{}","value2":"{}","value3":""}}'.format(arg1, arg2)
   command = "/usr/bin/curl -X POST -H 'Content-Type: application/json' -d '{}' {}".format(data, url)
   result = os.system(command)
   print(result)
else:
   raise Exception("Error. Key missing or not enough arguments given.")
