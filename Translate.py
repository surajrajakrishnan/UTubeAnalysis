# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:53:11 2019

@author: NDH00360
"""

# -*- coding: utf-8 -*-

# This simple app uses the '/translate' resource to translate text from
# one language to another.

# This sample runs on Python 2.7.x and Python 3.x.
# You may need to install requests and uuid.
# Run: pip install requests uuid

import os, requests, uuid, json


#if not key_var_name in os.environ:
 #   raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
subscription_key = "db7e7ced9e134bf687179d1e57550592"

#if not endpoint_var_name in os.environ:
 #   raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
endpoint = "https://youtubeanalytics.cognitiveservices.azure.com/sts/v1.0/issuetoken"

# If you encounter any issues with the base_url or path, make sure
# that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
path = '/translate?api-version=3.0'
params = '&to=de&to=it'
constructed_url = endpoint + path + params


headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-type': 'application/json',
    #'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text' : 'Hello World!'
}]
request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))
