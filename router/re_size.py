from fastapi import APIRouter,Request
from pydantic import BaseModel
from logic.re_size import re_size
from typing import List
import urllib.request
class Image(BaseModel):
    id: str
    url: str

class Images(BaseModel):
    images: List[Image]

router = APIRouter()

@router.post("/img")
def re_img(images: Images):
    '''

    '''
    response_list=[]
    for image in images.images:
        dict_response={}
        dict_response["id"]=image.id
        response=re_size(image.url,image.id)
        dict_response["img_encode"]=response
        response_list.append(dict_response)
    # We return the results
    return response_list

