from pfmqtt import Tx
from datetime import datetime
import time
import json

events = {}
t = Tx("d6f73930-cd18-4021-b28a-1d9a3e733333/6bfc17fb-3c55-4a29-81e7-c55089134ace", "mqtt.eclipse.org", "lol")

events.update(
        {str(datetime.timestamp(datetime.now())):
              {'x': 22, 'y': 33}
          }
)



events.update(
        {str(datetime.timestamp(datetime.now())):
              {'x': 22, 'y': 33}
          }
)


events.update(
        {str(datetime.timestamp(datetime.now())):
              {"x": 22, "y": 33}
          }
)

json_ting = json.dumps(events)
t.send_unenc(json_ting)



# TODO: Når der klikkes, skal events.update(ljashdflkajshdflkjhasdf) køres
# TODO: Hvert sekund gør det her:
# json_ting = json.dumps(events)
# t.send_unenc(json_ting)
# events.clear (tøm dict'en)