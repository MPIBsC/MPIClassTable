from icalendar import Calendar, Event
from datetime import datetime
from datetime import timedelta
from pytz import UTC
import json

SEM = '2017_2018-2'
PROG = '4LCDI'
YEAR = '1'
PROD = SEM + '_' + YEAR + '_' + PROG
classCode = '12221'
cal = Calendar()
cal.add('prodid', '-//MPIBsc//mxm.dk//' + PROD)
cal.add('version', '1.0')

fileIn = open('docs/data/class/2017_2018-2_1_4LCDI_en.json')
data = json.loads(fileIn.read())

for item in data:
    if item['class_code'][-5: ] == classCode:
        event = Event()
        event.add('summary', item['class_code'])
        event.add('description', item['subject'])
        dp = item['period'][0]
        tp = item['time'][0]
        dtstart = dp[0: dp.find('-')] + tp[0:tp.find('-')]
        dtend = dp[0: dp.find('-')] + tp[tp.find('-') + 1: ]
        rend = dp[dp.find('-') + 1:] + tp[tp.find('-') + 1: ]
        byday = ''
        for key, value in item['day'].iteritems():
            if value == 'true':
                byday = key

        if byday == 'mo':
            weekDay = 0
        if byday == 'tu':
            weekDay = 1
        if byday == 'we':
            weekDay = 2
        if byday == 'th':
            weekDay = 3
        if byday == 'fr':
            weekDay = 4
        if byday == 'sa':
            weekDay = 5
        if byday == 'su':
            weekDay = 6
        dtstart = datetime.strptime(dtstart, '%Y/%m/%d%H:%M')
        if dtstart.weekday() <= weekDay:
            dtstart += timedelta(days = weekDay - dtstart.weekday())

        print(item['class_code'] + ' ' + str(dtstart) + ' ' + byday)

        event.add('uid', item['class_code'] + byday + dp + tp + '@ipm.edu.mo')
        event.add('dtstamp', datetime.now())
        event.add('dtstart', dtstart)
        event.add('dtend', datetime.strptime(dtend, '%Y/%m/%d%H:%M'))
        event.add('location', item['room'][0])
        event.add('rrule', {'FREQ': "WEEKLY", 'BYDAY': byday, 'UNTIL': datetime.strptime(rend, '%Y/%m/%d%H:%M')})
        cal.add_component(event)

f = open('docs/calendar/' + PROD + '.ics', 'wb')
f.write(cal.to_ical())
f.close()
