from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/hello")
def hello():
    return JSONResponse(content={"message": "Hello Farook, what do you want?"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8501)
