from fastapi import FastAPI, Request, Form, Header
from fastapi.responses import FileResponse
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import json
app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
def 이름():
    return "보낼 값"


@app.get("/getCoordi")
async def getData(request : Request):
    json_string = '{'
    item_list = [111111, 111112, 111113]
    for i in range(0, 11):
        if i == 10:
            json_string += f'"coordi{i}":'+'{"item01":'+f'{item_list[0]}, "item02":{item_list[1]}, "item03":{item_list[2]}'+'}}'
        else:
            json_string += f'"coordi{i}":'+'{"item01":'+f'{item_list[0]}, "item02":{item_list[1]}, "item03":{item_list[2]}'+'},'
    print(json_string)
    data = json.loads(json_string)
    return JSONResponse(content = data)
