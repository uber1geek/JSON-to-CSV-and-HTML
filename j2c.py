import json
import csv
import pprint
from json2html import *

with open('data.json') as data_file:
    data = json.loads(data_file.read())


#pprint.pprint(data[0])

f = open("data.csv","wb")
c = csv.writer(f)


c.writerow(["ID","First Name","Last Name", "Email", "Gender", "IP"])

for d in data:
	c.writerow([str(d["id"]),str(d["first_name"]),str(d["last_name"]),str(d["email"]),str(d["gender"]),str(d["ip_address"])])

f.close()

print "Conversion Completed :)"

json_html = ''
for d in data:
    json_html += json2html.convert(json = d)
    #print json_html
    html_file= open("jsontable.html","w")
    html_file.write(json_html)
    html_file.close()
