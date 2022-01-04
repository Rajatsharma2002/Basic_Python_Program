
import requests
r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
a=r.text
print(r.text)
# print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)


def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

import json
# parse=json.dumps(a,indent=3)
# speak(parse)
