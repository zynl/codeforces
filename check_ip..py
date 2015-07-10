#!/bin/python
#python 3.4

import urllib.request
with urllib.request.urlopen ("http://freegeoip.net/csv/115.200.52.142") as f:
    print(f.read().decode('utf-8'))

#115.200.52.142,CN,China,33,Zhejiang Sheng,Hangzhou,,Asia/Shanghai,30.29,120.16,0

import urllib.request
with urllib.request.urlopen ("http://freegeoip.net/xml/115.200.52.142") as f:
    print(f.read().decode('utf-8'))
 
'''  
<?xml version="1.0" encoding="UTF-8"?>
<Response>
        <IP>115.200.52.142</IP>
        <CountryCode>CN</CountryCode>
        <CountryName>China</CountryName>
        <RegionCode>33</RegionCode>
        <RegionName>Zhejiang Sheng</RegionName>
        <City>Hangzhou</City>
        <ZipCode></ZipCode>
        <TimeZone>Asia/Shanghai</TimeZone>
        <Latitude>30.294</Latitude>
        <Longitude>120.161</Longitude>
        <MetroCode>0</MetroCode>
</Response>
'''
  
import urllib.request
with urllib.request.urlopen ("http://freegeoip.net/json/115.200.52.142") as f:
    print(f.read().decode('utf-8'))

'''
    "ip":"115.200.52.142",
    "country_code":"CN",
    "country_name":"China",
    "region_code":"33",
    "region_name":"Zhejiang Sheng",
    "city":"Hangzhou",
    "zip_code":"",
    "time_zone":"Asia/Shanghai",
    "latitude":30.294,
    "longitude":120.161,
    "metro_code":0
    }
'''
