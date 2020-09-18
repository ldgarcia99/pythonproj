# How many total requests have been made in the last year?
# How many total requests were made in the time period represented by the log?
# 12 Oct 1994 through 12 Oct 1995
import os
import re

f = open('http_access_log', 'r')




def reader(http_access_log):
with open(http_access_log) as h:
  log = h.read()
  print(log)

URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local = 'http_access_log'

def fileCount():
    filelog = []
    selectdates = []
    allrequests = []

    with open(local) as logs:
 		for line in logs:
 			try:
 				filelog.append(line[line.index("GET")+4:line.index("HTTP")])
 			except:
 				pass

    for count in counter.selectdates

    selectdates = ("Oct/1994, Nov/1994, Dec/1994, Jan/1995, Feb/1995, Mar/1995, Apr/1995, May/1995, June/1995,
                    July/1995, Aug/1995, Sep/1995, Oct/1995, Nov/1995, Dec/1995")


    counter = collections.Counter(filelog)
 	  for count in counter.selectdates(1):
 		       print("The requests with selected dates are".format(str(count[0]), str(count[1])))

 				   print(file)


    counter = collections.Counter(filelog)
        for count in counter.allrequests
            count = allrequests
        print("There were % total requests.")
