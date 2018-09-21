# -*- coding: utf-8 -*-
import json
import urllib2

amap_api_key = "eb812947974ec114453944dd9e7c11ca"

address_to_gps_api_url_module = "http://restapi.amap.com/v3/geocode/geo?key=%(key)s&address=%(address)s"


def read_url(url):
    return urllib2.urlopen(url).read()


def address_to_gps(address):
    return json.loads(read_url(address_to_gps_api_url_module % {
        "key": amap_api_key,
        "address": address.encode("UTF-8")
    }))
