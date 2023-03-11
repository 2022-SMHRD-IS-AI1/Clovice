from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
app = FastAPI()

class Model(BaseModel):
    id : str
    pw : str
    name : str
    ssn : int
    email : str
    phone : str

@app.get("/")
def 이름():
    return "보낼 값"

@app.get("/second")
def 두번째():
    return {"군단장" : "아브렐"}

@app.get("/html")
async def getHtml():
    return FileResponse('Clovice/Beautiflie Free Website Template - Free-CSS.com/html/join.html')

@app.post("/send")
async def getData(data : Model):
    print(data)
    return '전송완료'