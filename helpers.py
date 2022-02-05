
import datetime
import base64
import time
from io import BytesIO
from PIL import Image
from fractions import Fraction

DATETIME_STR_FORMAT = "%Y-%m-%d_%H:%M:%S.%f"


def get_now_string() -> str:
    return datetime.datetime.now().strftime(DATETIME_STR_FORMAT)

def base64_to_pil(image_base64):
    return Image.open(BytesIO(base64.b64decode(image_base64)))


def buffer_to_base64(image_buffer, encoding='utf-8'):
    return base64.b64encode(image_buffer.getvalue()).decode(encoding)

def pil_to_base64(image_pil, encoding='utf-8'):
    image_buffer = BytesIO()
    image_pil.save(image_buffer, format='JPEG')
    return buffer_to_base64(image_buffer, encoding=encoding)