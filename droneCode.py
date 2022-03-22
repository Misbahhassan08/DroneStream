import cv2
import jetson.inference
import jetson.utils
import time
import os
import cv2
import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5566")
time.sleep(1)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

model = "ssd-mobilenet-v1"
model_th = 0.7


net = jetson.inference.detectNet(model, model_th)
camera = cv2.VideoCapture(0)
display = jetson.utils.videoOutput()


while True:
    message = socket.recv()
    print("Received request: %s" % message)
    try:
        ret, frame = camera.read()
        # convert to CUDA (cv2 images are numpy arrays, in BGR format)
        bgr_img = jetson.utils.cudaFromNumpy(frame, isBGR=True)
        rgb_img = jetson.utils.cudaAllocMapped(width=bgr_img.width,
                                    height=bgr_img.height,
                                    format='rgb8')

        jetson.utils.cudaConvertColor(bgr_img, rgb_img)
        detections = net.Detect(rgb_img)
        if len(detections) > 0:

            for detection in detections:
                label = net.GetClassDesc(detection.ClassID)
                x1 = int(detection.Left)
                y1 = int(detection.Top)
                x2 = int(detection.Right)
                y2 = int(detection.Bottom)
                frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (23, 250, 44),1)
                frame = cv2.putText(frame, label, (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                #frame = cv2.resize(frame,(440,440))
                retval, buffer = cv2.imencode('.png', frame)
                data = buffer.tobytes()
                socket.send(data)
        else:
            socket.send(b'None')
        cv2.imshow("window", frame)
        cv2.waitKey(10)
    except:
        pass
    

    pass # end of main loop 
