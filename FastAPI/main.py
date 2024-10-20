from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 입력받을 데이터 모델 정의 (Pydantic BaseModel 사용)
class StringInput(BaseModel):
    input_string: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/getTest")
async def getTest():
    return {"testField": "This data come from /getTest"}

# POST 엔드포인트 정의
@app.post("/postTest")
async def postTest(data: str):
    return {"testField": f"This data come from /postTest => {data}"}