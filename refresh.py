import urllib
import json
from BeautifulSoup import BeautifulSoup

BASEURL = "https://wapps.ipm.edu.mo/siweb/time_prog.asp"
YEAR_SEM = "2017/2018-2"
html = urllib.urlopen(BASEURL).read()
parsedHtml = BeautifulSoup(html)
parseFile('p_escl_cod','school', parsedHtml)
parseFile('p_curso','programs', parsedHtml)

def parseFile(attr, fileName, html):
    data = []
    innerHtml = parsedHtml.body.find('select', attrs={'name': attr})
    for item in innerHtml.findChildren():
        for key, value in item.attrs:
            if value and value != "selected" :
                data.append({"value": value, "label": item.text})
    f = open('docs/data/' + fileName + '.json', 'w')
    f.write(json.dumps(data))
    f.close()

def parseTimeTable(program, spYear):
    params = urllib.urlencode(
        {'p_curso': program,
         'p_sp_year': spYear,
          'Submit2': 'Search',
          'action': 'search',
          'la': 'en',
          'p_year_sem': YEAR_SEM})
    html = urllib.urlopen(BASEURL, params)
    parsedHtml = BeautifulSoup(html)
    innerHtml = parsedHtml.body.find('table', attrs={'bordercolor': '#CCCCCC'})
    # for course in innerHtml.findChildren():
    #     for item in course.findChildren():
    #         print (item)

parseTimeTable('4LACDI', 1)
