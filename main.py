import tweepy
from tweepy import OAuthHandler
from tweepy import API
import datetime as dt
import  time
from os import environ
import json
from datetime import datetime,timedelta
import pandas as pd
import requests

url = 'https://notify-api.line.me/api/notify'
token = 'YxnlWf0UZjJioWuSjilvEqxtEWd2kfhME8sc8umqZ3A'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}


msg ='Program runnning'
