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

rapid.listen("Slack", "slashCommand", {"token": "POXHiHLeABGAGZJKcLBUGjZb", "command": "/barak-test"}, on_join=on_join, on_message=on_message, on_close=on_close)

rapid.listen("Slack", "slashCommand", {"token": "gwuFIMT8ZmhJvaJcwrBW1FDe", "command": "/qatest"}, on_join=on_join, on_message=on_message, on_close=on_close)
