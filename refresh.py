import requests
import subprocess
import urllib
import json
import pprint
import sys
import os
from BeautifulSoup import BeautifulSoup

BASEURL = "https://wapps.ipm.edu.mo/siweb/time_prog.asp"
YEAR_SEM = "2018/2019-1"
YEAR_SEM_FN = "2018_2019-1"

def parseFile(attr, fileName, html):
    data = []
    innerHtml = html.body.find('select', attrs={'name': attr})
    for item in innerHtml.findChildren():
        for key, value in item.attrs:
            if value and value != "selected" :
                data.append({"value": value, "label": item.text})
    f = open('docs/data/' + fileName + '.json', 'w')
    f.write(json.dumps(data))
    f.close()

def runCat():
    cmd = 'curl ' + BASEURL + ' --tlsv1.0'
    html = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
    parsedHtml = BeautifulSoup(html)
    parseFile('p_escl_cod','school', parsedHtml)
    parseFile('p_curso','programs', parsedHtml)

def parseTimeTable(lang, program, spYear):
    params = urllib.urlencode(
        {'p_curso': program,
         'p_sp_year': spYear,
          'Submit2': 'Search',
          'action': 'search',
          'la': lang,
          'p_year_sem': YEAR_SEM})
    print(params)

    cmd = 'curl -d "' + params + '" ' + BASEURL + ' --tlsv1.0'
    html = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
    parsedHtml = BeautifulSoup(html)
    innerHtml = parsedHtml.body.find('table', attrs={'bordercolor': '#CCCCCC'})
    prevIndex = 1
    prevData = {}
    totalData = []
    for course in innerHtml.findAllNext('tr')[2: -5]:
        info = course.findChildren('font')
        length = len(info)
        indent = length <= 12 and info[0].text == u'&nbsp;'
        offset = 3 if indent else 0
        data = {
            'year': prevData['year'] if indent else info[0].text,
            'type': prevData['type'] if indent else info[1].text,
            'class_code': prevData['class_code'] if indent else info[2].text,
            'subject': prevData['subject'] if indent else info[3].text,
            'instructor': info[4 - offset].text,
        }
        if length >= 12:
            data['room'] = info[5 - offset].text,
            data['period'] = info[6 - offset].text,
            data['time'] = info[7 - offset].text,
            data['day'] = {
                    'su': 'false' if info[8 - offset].text == u'&nbsp;' else 'true',
                    'mo': 'false' if info[9 - offset].text == u'&nbsp;' else 'true',
                    'tu': 'false' if info[10 - offset].text == u'&nbsp;' else 'true',
                    'we': 'false' if info[11 - offset].text == u'&nbsp;' else 'true',
                    'th': 'false' if info[12 - offset].text == u'&nbsp;' else 'true',
                    'fr': 'false' if info[13 - offset].text == u'&nbsp;' else 'true',
                    'sa': 'false' if info[14 - offset].text == u'&nbsp;' else 'true',
                }
        else:
            data['info'] = info[5 - offset].text
        if length == 15:
            prevData = {
                'year': info[0].text,
                'type': info[1].text,
                'class_code': info[2].text,
                'subject': info[3].text,
            }
        totalData.append(data)
    f = open('docs/data/class/' + YEAR_SEM_FN + '_' + str(spYear) + '_' + program + '_' + lang + '.json', 'w')
    f.write(json.dumps(totalData))
    f.close()

def runTimeTbl(lang):
    prog = open("docs/data/programs.json")
    for program in json.loads(prog.read()):
        pro = program['value']
        for i in range(1, 5):
            print("\033[92mReading " + pro + " class " + str(i))
            try:
                parseTimeTable(lang, pro, i)
            except:
                print("\033[91mAn error arised in reading " + pro + str(i))
                f = open('docs/data/error.log', 'w+')
                f.write("Error in reading" + pro + " " + str(i) + "\n" + str(sys.exc_info()[0]) + "\n")
                f.close()

def purifyData():
    for filename in os.listdir('docs/data/class/'):
        with open('docs/data/class/' + filename) as f:
            print("\033[92mProcessing " + filename)
            newText=f.read().replace('&nbsp;', '')

        with open('docs/data/class/' + filename, "w") as f:
            print("\033[92mWriting to " + filename)
            f.write(newText)
#runCat()
runTimeTbl('en')
# runTimeTbl('ch')
purifyData()
