import urllib
import json
from BeautifulSoup import BeautifulSoup

BASEURL = "https://wapps.ipm.edu.mo/siweb/time_prog.asp"
html = urllib.urlopen(BASEURL).read()
parsedHtml = BeautifulSoup(html)

def parseFile(attr, fileName, html):
    itemDict = {}
    innerHtml = parsedHtml.body.find('select', attrs={'name': attr})
    for item in innerHtml.findChildren():
        for key, value in item.attrs:
            if value:
                itemDict[value] = item.text

    f = open('docs/data/' + fileName + '.json', 'w')
    f.write(json.dumps(itemDict))
    f.close()

parseFile('p_escl_cod','school', parsedHtml)
parseFile('p_curso','programs', parsedHtml)
