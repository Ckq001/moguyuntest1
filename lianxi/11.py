#!/usr/bin/python
# -*- coding: UTF-8 -*-



import requests
from requests.packages import urllib3
urllib3.disable_warnings()

# import logging
# logging.captureWarnings(True)
url = 'https://test-pg.cailian.net/api/login'
payload = 'loginName=15003882332&password=54db60f921c24fed6ff5d8604a73862c&kaptchaCode=1111'
headers = {
  'Accept': 'application/json, text/plain, */*',
  'Content-Type': 'application/x-www-form-urlencoded'
}
response = requests.request('POST', url, headers = headers, data = payload,verify=False)
print(response.text)