import requests
import base64
import json

'''
response sample:
{
   "books_search":{
      "@xmlns":"http://www.ourmoviest.com/mv",
      "@xmlns:xsi":"http://www.w3.org/2001/XMLSchema-instance",
      "@xsi:schemaLocation":"http://www.bookie.com/mv mv.xsd ",
      "error":{
         "errorMessage":"bookid was not found",
         "statusCode":"00554"
      }
   }
}
'''


url = r""{{ your url}}""
authKey = base64.b64encode("username:pwd")
headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}
data = { "idofelement":some_value}

r = requests.get(url, headers=headers, params = data)
j_object = r.json()
try:

    print r.json()['books_search']['error']
except:
    print "ok"
