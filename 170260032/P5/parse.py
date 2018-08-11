import json
import csv

data =''
with open('infinity_stones.json','r') as rfile:
    data = json.load(rfile)
with open('infinity_stones.csv', 'w') as wfile:
    wrtr = csv.writer(wfile,delimiter='|')
    wrtr.writerow(['','Stone Name','Stone Color','Containment Unit',''])
    for key,value in data.items():
        for val in value:
            wrtr.writerow(['',val['Stone Name'],val['Stone Color'],val['Containment Unit'],''])
