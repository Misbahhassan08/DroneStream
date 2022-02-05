import json
from matplotlib.font_manager import json_load
import requests
from io import BytesIO
from PIL import Image
import datetime
import base64

def base64_to_pil(image_base64):
    return Image.open(BytesIO(base64.b64decode(image_base64)))


x = requests.get('http://192.168.10.33:5000/getImage')
mesg = json.loads(x.text)
img = mesg['image']
data = mesg['data']

img = base64_to_pil(img)
img.show()
print(img)