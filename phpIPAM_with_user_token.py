#!/usr/bin/env python

import requests
import json
import sys
import csv

server     = "http://SERVER_ADDRESS"
appid      = "APP_ID"
username   = "USERNAME"
password   = "PASSWORD"
url        = sys.argv[1]
url_split  = url.split("/")
url_length = len(url_split)

url_for_file_name = ''

if url_length > 1:
    i = 1
    for i in range(url_length):
        url_for_file_name =  url_for_file_name + '_' + url_split[i]
else:
    url_for_file_name   = '_' + url_split[0]

baseurl = server + "/api/" + appid
res = requests.post(baseurl + '/user/', auth=(username, password))
token = json.loads(res.content)['data']['token']
res = requests.get(baseurl + '/' + url + '/', headers={'token': token})

rawdata = json.loads(res.content)
if 'data' in rawdata:
    api_data = rawdata['data'] 
    api_data_file = open('phpIPAM' + url_for_file_name + '.csv', 'w') 
    csv_writer = csv.writer(api_data_file) 

    count = 0
  
    for dt in api_data: 
        if count == 0: 
            header = dt.keys() 
            csv_writer.writerow(header) 
            count += 1

        csv_writer.writerow(dt.values()) 
  
    api_data_file.close() 
