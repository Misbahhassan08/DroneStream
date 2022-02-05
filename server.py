import json
from PIL import Image
from helpers import pil_to_base64, base64_to_pil
from flask import Flask
import cv2
import time

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)


@app.route('/getImage', methods = ['GET'])
def messageToTopic():
    cap = cv2.VideoCapture(0)
    time.sleep(1)
    ret, frame = cap.read()
    cv2.imwrite("img.jpg", frame)
    img = Image.open("img.jpg")
    b64_img = pil_to_base64(img)
    output = {
            'image' : b64_img,
            'data':'Image from server'
            }
    output_json = json.dumps(output)
    return output_json
    pass # end of messageToTopic(params) function

# main driver function
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)