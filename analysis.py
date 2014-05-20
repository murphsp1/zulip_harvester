import json
import datetime
import itertools
#from matplotlib.dates import drange, num2date
from dateutil.rrule import rrule, DAILY


'''
This module is concerned with running analysis on the data saved to json
by the harvester.py module
'''


'''
There is some question as to the separation of data acquisition, cleaning, and analysis.
Where does each of these functionalities go as we transition from analysis to reproducibility

'''


'''
First analysis
Want to count up all messages by date to get a total
Want to count up all messages by date and by stream to get a total
Might make sense to start looking at things in a Panda data frame (a large
pandas data frame, but one nonethe less)
'''

flattened_messages = []
for stream_name, stream in data.iteritems():
    for m in stream:
        m['stream'] = stream_name
        d = convert_from_unixtime(m['timestamp'])
        m['datetime'] = d #.strftime('%Y%m%d-%H%M')
        flattened_messages.append(m)


list_of_dates = [m['datetime'].date() for m in flattened_messages]

dates = list(rrule(DAILY, dtstart=min(list_of_dates), until=max(list_of_dates) ) )

date_counts = []

for d in dates:
    date_counts.append( list_of_dates.count(d.date()))
