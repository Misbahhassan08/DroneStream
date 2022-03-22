# change the IP address of your drone before using this code

import zmq
import numpy as np
import cv2
import time
context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.10.11:5566") # change IP address here

#  Do 10 requests, waiting each time for a response
while True:
    print("Sending request ")
    socket.send(b"Message from Ground Station")
    try:
        #  Get the reply.
        frame = socket.recv()
        if frame == b'None':
            pass
        else:
            image = np.asarray(bytearray(frame), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            cv2.imwrite('1.png',image)
            #time.sleep(4)
    except Exception as error:
        print(error)
