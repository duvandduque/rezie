# Author: Juan Sebastián Ramírez
# This main would be used for fastAPI implementation of face blurring

# We import fastAPI
from fastapi import FastAPI

from router.re_size import router as face_blurrer
from router.home import router as home

# We import the class
app = FastAPI()
app.include_router(home)
app.include_router(face_blurrer)