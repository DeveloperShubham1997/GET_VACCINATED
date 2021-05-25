import requests
import datetime
from fake_useragent import UserAgent
import time
from telegram import toTelegram

temp_user_agent = UserAgent()
browser_header = {'User-Agent': temp_user_agent.random}



store=[]
def find_vaccine(district_id,date):
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="+district_id+"&date="+date
    response = requests.get(URL, headers=browser_header)
    if response.ok:
        resp_json = response.json()
        #print(resp_json)
        for j in resp_json["sessions"]:
            if(j["available_capacity_dose1"]>=0):
                centers = []

                
                centers.append("name: "+j["name"])
                centers.append("address: "+j["address"])
                centers.append("pincode: "+str(j["pincode"]))
                centers.append("date: "+j["date"])
                centers.append("min_age_limit: "+str(j["min_age_limit"]))
                centers.append("available_capacity_dose1: "+str(j["available_capacity_dose1"]))
                tosend='\n'.join(centers)
                

                if(tosend not in store):
                	store.append(tosend)
                	toTelegram(tosend)

