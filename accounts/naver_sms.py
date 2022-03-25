import time
import requests
import hashlib
import hmac
import base64
from django.conf import settings

def send_sms(phone_number, message):

  def make_signature(access_key, secret_key, method, uri, timestamp):
    secret_key = bytes(secret_key, 'UTF-8')

    message = method + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
    return signingKey

  services_id = settings.NAVER_SERVICES_ID
  url = f'https://sens.apigw.ntruss.com/sms/v2/services/{services_id}/messages'
  access_key = settings.NAVER_ACCESS_KEY_ID
  secret_key = settings.NAVER_SECRET_KEY
  uri = f'/sms/v2/services/{services_id}/messages'
  timestamp = str(int(time.time() * 1000))

  body = {
    "type":"SMS",
    "contentType":"COMM",
    "countryCode":"82",
    "from":"01038336177",
    "content": message,
    "messages":[
        {
            "to": phone_number,
        }
    ]
  }

  key = make_signature(access_key, secret_key, 'POST', uri, timestamp)
  headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'x-ncp-apigw-timestamp': timestamp,
    'x-ncp-iam-access-key': access_key,
    'x-ncp-apigw-signature-v2': key
  }

  res = requests.post(url, json=body, headers=headers)
  print(res.json())
  return res.json()