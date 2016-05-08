import requests
import json
import pprint


def makeRequest(text):
    req = {
        "user_key": "sample1234",
        "type": "text",
        "content": text
    }
    return req


def sendMessage(url, text):
    r = requests.post(url, json=makeRequest(text))
    print(r.json())


url = "http://localhost:5000/message"

while True:
    t = input("메시지 입력 : ")
    sendMessage(url, t)
