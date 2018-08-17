import json

with open('infinity_stones.json','r') as rfile:
    data = json.load(rfile)
with open('update_stones.json', 'w') as wfile:
    for key,value in data.items():
        for val in value:
            val['Stone Name'] = val['Stone Name']
            val['Stone Color'] = val['Stone Color']
            val['Containment Unit'] = 'Infinity Gauntlet'
    json.dump(data, wfile, indent=4)
