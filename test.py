# -*- coding: utf-8 -*-

from rapidconnect import RapidConnect
import logging

logging.info("TEST")

rapid = RapidConnect('lightbringer', '3dab63eb-4166-4315-81f5-f7c79164d31f');
result = rapid.call('MicrosoftComputerVision', 'describeImage', {
    'image': 'https://s15.postimg.org/id184l9t7/image.jpg',
    'subscriptionKey': 'a04b26d206e2482083db92c60b3b818a',
    'maxCandidates': ''

});
print result