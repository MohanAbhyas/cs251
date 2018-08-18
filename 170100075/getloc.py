#! /usr/local/bin/python
import json
import requests
import datetime
def iss_location():
	url="http://api.open-notify.org/iss-now.json"
	wbpage=requests.get(url)
	obj=json.loads(wbpage.content) 
	print("Current Location of ISS:")
	print("Latitude :",obj["iss_position"]["latitude"])
	print("Longitude :",obj["iss_position"]["longitude"])
def pass_time():
	url2="http://api.open-notify.org/iss-pass.json"
	param={}
	request={}
	print("Enter Details to know when ISS will pass over a location:")
	request["lat"]=float(input("Latitude :"))
	request["lon"]=float(input("Longitude :"))
	wbpage=requests.get(url2,params=request)
	obj2=json.loads(wbpage.text)
	risetime=datetime.datetime.utcfromtimestamp(obj2["response"][0]["risetime"])
	duration=datetime.datetime.utcfromtimestamp(obj2["response"][0]["duration"])
	print("Date :",risetime.strftime('%d/%m/%Y'))
	print("Time :",risetime.strftime('%H:%M'))
	print("For :",duration.strftime('%M minutes and %S seconds'))

def people_info():
	url3="http://api.open-notify.org/astros.json"
	wbpage3=requests.get(url3)
	obj3=json.loads(wbpage3.content)
	print("People currently in space:",obj3["number"])
	for people in obj3["people"]:
		print(people["name"])
iss_location()
pass_time()
people_info()

