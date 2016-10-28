# -*- coding: utf-8 -*-
"""Extract the cantons blbalabla"""

import requests
import json

import pandas as pd

""" Define the url for the geonames API and the username"""
url = "http://api.geonames.org/search?"
username = 'cataphile22'

def extractCanton(dataframe, q, raw = None):
    """Try to find the canton of the string given in arg (typically a university name). Beware this function is performing a request to geonames.
    The parameter dataframe is the dataframe created from the cvs file ExtractGrant"""
    if raw == None: # if raw is not set, it is equal to q
        raw = q
    param = {'q': q, 'country': 'CH', 'type': 'json'  ,'username': username}
    
    res = requests.get(url, params=param)
    df_ = pd.read_json(res.content)
    if df_.geonames.count() > 0 :
        df_.geonames[0]['adminCode1']
        dataframe['Canton'][(dataframe['Canton'] == "") & (dataframe['University'] == raw)] = df_.geonames[0]['adminCode1']
    return
