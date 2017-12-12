from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC
import json

cal = Calendar()
cal.add('prodid', '-//MPIBsc//mxm.dk//' + '2017_2018-2_1_4LCDI')
cal.add('version', '1.0')

fileIn = open('docs/data/class/2017_2018-2_1_4LCDI_en.json')
data = json.loads(fileIn.read())

for item in data:
    if item['class_code'][-5: ] == '12221':
        event = Event()
        event.add('summary', item['subject'])
        dp = item['period'][0]
        tp = item['time'][0]
        dtstart = dp[0: dp.find('-')] + tp[0:tp.find('-')]
        dtend = dp[0: dp.find('-')] + tp[tp.find('-') + 1: ]
        rend = dp[dp.find('-') + 1:] + tp[tp.find('-') + 1: ]
        byday = []
        for key, value in item['day'].iteritems():
            if value == 'true':
                byday.append(key)
        event.add('dtstamp', datetime.now())
        event.add('dtstart', datetime.strptime(dtstart, '%Y/%m/%d%H:%M'))
        event.add('dtend', datetime.strptime(dtend, '%Y/%m/%d%H:%M'))
        event.add('location', item['room'][0])
        event.add('rrule', {'FREQ': "WEEKLY", 'BYDAY': byday, 'UNTIL': datetime.strptime(rend, '%Y/%m/%d%H:%M')})
        cal.add_component(event)

f = open('example.ics', 'wb')
f.write(cal.to_ical())
f.close()
