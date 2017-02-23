# -*- coding: utf-8 -*-

from rapidconnect import RapidConnect

rapid = RapidConnect("testa", "a3787239-bb1e-4fa4-85c3-a423fa6af51f")

result = rapid.call("GoogleTranslate", "translate", {
    'string': 'שלום',
    'sourceLanguage': 'he',
    'targetLanguage': 'en',
    'apiKey': 'XXXX'

})

print result

def on_join():
    print("joined!")

def on_message(message):
    print(message)

def on_close():
    print("Closed!")

def on_error(message):
    print("error:")
    print(message)
    
res = rapid.listen("Slack", "slashCommand", {"token": "ydt3vFyVEoW51ZFCC2i5QKab", "command": "/send_test"}, on_join=on_join, on_message=on_message, on_close=on_close)
j = res.json()
print j["token"]
