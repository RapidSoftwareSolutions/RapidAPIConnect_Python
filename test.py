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
