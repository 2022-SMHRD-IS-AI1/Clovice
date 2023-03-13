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
    json_string = '{"name":"gsj", "age":21, "gender":"male"}'
    data = json.loads(json_string)
    return JSONResponse(content = data)
