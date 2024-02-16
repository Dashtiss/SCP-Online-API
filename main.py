import argparse
import os
import settings


from fastapi import FastAPI
from typing import Union
app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}
