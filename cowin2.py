import requests
import datetime
import json

from fake_useragent import UserAgent

temp_user_agent = UserAgent()
browser_header = {'User-Agent': temp_user_agent.random}




#POST_CODE = "751003"
age = 20



numdays = 1
base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]

AllpincodesKhurdha = [751001, 752103, 752021, 751022, 752021, 751020, 751019, 751020, 752103, 752060, 751003, 752054,752030, 752031,752066,752064,752050,752064,751009,752102,752035,751014,752061,751018,752030,752023,752031,752050,752031,752061,752055,752060,752019,752100,752101,752031,752102,752030,752030,752103,752056,752066,751002,752031,752035,751009,752066,752034,752027,751003,752062,752034,752062,752030,752101,752100,752103,752103,751003,752019,752115, 752031, 751020, 751002, 752031, 752050,752061,751022,752061,751014,751001,751009,752021,752020,752027,752102,752066,752038,752100]


for POST_CODE in AllpincodesKhurdha: 
   for INP_DATE in date_str:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(POST_CODE, INP_DATE)
        response = requests.get(URL, headers=browser_header)
        if response.ok:
           resp_json = response.json()
           flag = False
           
           if resp_json["centers"]:
              for center in resp_json["centers"]:
                  vaccineAvailable=0
                  for session in center["sessions"]:
                      #print ("sessions-----")
                      if session["min_age_limit"] <= age:
                          #print("\t", center["name"])
                          #print("\t", center["block_name"])
                          #print("\t Price: ", center["fee_type"])
                          #print("\t Available Capacity: ", session["available_capacity"])
                          vaccineAvailable=vaccineAvailable+session["available_capacity"]
                  if vaccineAvailable>0:
                      print ("centre--> ", center["name"],"-----Available shots--> ", vaccineAvailable,"-----Date--> ", INP_DATE,"----Pincode--->", POST_CODE)                 







































