import requests
from PIL import Image
from io import BytesIO
import base64
from os import remove

def re_size(url,id):
    im = Image.open(requests.get(url, stream=True).raw)
    new_image = im.resize((500, 500))
    filename=id+".png"
    new_image.save(filename)
    base64_bytes=""
    with open(filename, 'rb') as image_file:
        base64_bytes = base64.b64encode(image_file.read())
        print(base64_bytes)
    remove(filename)
    #print(base64_bytes)
    return base64_bytes