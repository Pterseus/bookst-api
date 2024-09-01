from fastapi import FastAPI, UploadFile
from mangum import Mangum
from mark_json import from_mark

app = FastAPI()

@app.get("/")
async def root():
  return 'OK'

@app.post("/parse")
async def markdown_to_json(file: UploadFile):
  content = await file.read()
  markdown_content = content.decode('utf-8')

  parsed_data = from_mark(markdown_content)

  return {"data": parsed_data}

handler = Mangum(app, lifespan="off")