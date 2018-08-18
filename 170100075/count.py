#! /usr/local/bin/python
import csv
import requests
from bs4 import BeautifulSoup
url="https://www.cse.iitb.ac.in/page222"
content=requests.get(url)
Bcontent = BeautifulSoup(content.content,'html.parser')
content3=Bcontent.find(id="ddsubmenu_people")
content4=content3.find('a',text="Students")
links=[]
data={}
for g in content4.parent.ul.find_all('a'):
	data[g.get_text()]=url+g.get('href').replace("page222","")

for category,link in data.items():
	indicontent=requests.get(link)
	content=BeautifulSoup(indicontent.content,'html.parser')
	content3=content.find('table')
	data[category]=len(content3.findChildren('tr',recursive=False))

with open('count.csv', 'w') as wfile:
	writer = csv.writer(wfile,delimiter=',')#,quotechar="'")
	writer.writerow(['Category Name','No. of students'])
	for k,v in data.items():
		writer.writerow([k,v])
