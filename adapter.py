import cgp_core
import cgp_zmq
import json
import time
import threading
from newplot import *

# Adapter class deriveed from cgp_core.Adapter
class Adapter(cgp_core.Adapter):
    # on_consume method to expect the Action data from Application
    def on_consume(self, requests):
        #print requests
        a = cgp_core.ReactionData('')
        for request in requests:
            number = request['trackingId'].split("-")
            a1 = get_json_line(int(number[0]))

            a.add('Tag00', [a1], request['contextUri'], request['contextPrefix'], 0, request['trackingId'], 'testData', 5000, 0, None, None)
        self.send_response(a)

if __name__ == "__main__":
    # connect Adapter to Gateway Manager
    adap = Adapter()
    comms = cgp_zmq.AdapterComm('adp1', 'tcp://127.0.0.1:3000')
    comms.instrument = adap