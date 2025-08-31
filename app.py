from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/hello")
def hello():
    return JSONResponse(content={"message": "Hello Farook, You can see your dashboard reports on http://localhost:3000/"})
