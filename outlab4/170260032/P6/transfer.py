import json
import random

tns = []
for i in range(ord('A'), ord('J')+1):
    tns.append(chr(i))
jns = []
for i in range(1, 1001):
    jns.append(i)
random.shuffle(jns)
jns = jns[:100]
lns = []
for i in range(1,101):
    lns.append(random.randint(1,10))
database = {}
teamlist = []
playerlist = []
tempdict1 = {}
tempdict2 = {}
k = 0
for i in tns:
    for j in range(k, k+10):
        #tempdict1 = {"Jersey Number":jns[j], "Loyalty":lns[j]}
        tempdict1[str(jns[j])] = str(lns[j])
        #playerlist.append(tempdict1)
    k = k+10
    #tempdict2[i] = playerlist
    tempdict2[i] = tempdict1
    #playerlist = []
    tempdict1 = {}
database['Teams'] = tempdict2
with open('playerDatabase.json', 'w') as wfile:
    json.dump(database, wfile, indent=4)
with open("transfer.txt", 'r') as rfile:
    count = 0
    i = rfile.readline()
    while i:
        if i.split(" ")[0] != 'Team_name':
            team,jnbr = i.split()
            #print(team +' '+str(jnbr))
            if team not in tns:
                pass #print("Try another transfer(Wrong team name)")
            else:
                tm1='Z'
                tm2=team
                for j in database['Teams'].keys():
                    #print('j',j)
                    #print(jnbr)
                    #print('p', database['Teams'][j].keys())
                    for l in database['Teams'][j].keys():
                        if str(jnbr) == str(l):
                            tm1=j
                            break
                    #print("tm1", tm1)
                if tm1 not in tns:
                    pass #print("Try another transfer(Wrong player name)")
                elif tm1 == tm2:
                    pass #print("Player is in the same team")
                elif int(database['Teams'][tm1][jnbr]) > 7:
                    pass #print("Try another transfer(Players rating greater than 7 cannot be transfered)")
                else:
                    minl,minp = 11,''
                    for j in database['Teams'][tm2].keys():
                        if int(minl) > int(database['Teams'][tm2][j]):
                            minp = j
                            minl = database['Teams'][tm2][j]
                    if int(minl) > 7:
                        pass #print("Try another transfer(Team chosen cannot return player)")
                    else:
                        database['Teams'][tm1][minp] = minl
                        database['Teams'][tm2][jnbr] = database['Teams'][tm1][jnbr]
                        del database['Teams'][tm1][jnbr]
                        del database['Teams'][tm2][minp]
                        #print("Tranfer Complete")
                        count = count + 1
        i = rfile.readline()
    print("Players transfered ", count)
with open('modifiedDatabase.json', 'w') as wfile:
    json.dump(database, wfile, indent=4)
