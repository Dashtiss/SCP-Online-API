import settings
import os
import ServerThings.Server

try:
    import fastapi
except ImportError:
    print("\033[31mError: \033[0mMissing dependencies.")
    Install = input("Would you like to install the dependencies? (y/n)    ")
    if Install.lower() == "y":
        os.system('pip install fastapi "uvicorn [standard]"')
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


async def SaveServers():
    data = {}
    with open("Save.json", "w") as File:
        import json
        for Server in servers:
            data[Server.ServerID] = {}
            data[Server.ServerID]["Name"] = Server.ServerName
        json.dump(data, File)


app = FastAPI()

servers: list[ServerThings.Server.Server] = []


@app.get("/")
async def home():
    return {"Not": "Here"}


@app.post("/api/v1/addserver")
async def AddServer(ServerDescription: ServerThings.Server.Server):
    try:
        if ServerDescription in servers:
            return 1025
        servers.append(ServerDescription)
        await SaveServers()
        return {"Arrived": True}
    except Exception as E:
        return {"Error": E.args}


@app.get("/api/v1/getserver")
async def GetServer(ServerName: str):
    for Server in servers:
        if ServerName == Server.ServerName:
            return {ServerName: Server.ServerInfo}
    return {"Error": 1026}


@app.get("/api/v1/listServers")
async def listServers():
    return {"Servers": servers}


@app.post("api/v1/pec")
async def ParseErrorCode(Code: int):
    """will take in an error code and parse it to its meaning"""
    ErrorCodes = {
        1025: "Error: Server already Exists in the database",
        1026: "Error: Server does not exist"
    }
    if Code in ErrorCodes.keys():
        return {Code: ErrorCodes[Code]}
    else:
        return {"Error": "Code not found"}
