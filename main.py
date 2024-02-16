import settings
import os
import ServerThings.Server

try:
    import fastapi
except ImportError:
    print("\033[31mError: \033[0mMissing dependencies.")
    Install = input("Would you like to install the dependencies? (y/n)    ")
    if Install.lower() == "y":
        os.system('pip install fastapi "uvicorn[standard]"')
        print("-" * 10)
        print("Dependencies installed.")
        try:
            import fastapi
        except ImportError:
            print(
                "\033[31mError: \033[0mDependencies didn't install properly please check console for more information")
            exit(1)

from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
def home():
    return


@app.post("/addserver")
def AddServer(ServerDescription: ServerThings.Server.Server):
    return ServerDescription
