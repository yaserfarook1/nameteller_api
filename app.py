import streamlit as st
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from streamlit.web.server import server

# Create FastAPI app
app = FastAPI()

@app.get("/hello")
def hello():
    return JSONResponse(content={"message": "Hello Farook, what do you want?"})

# Mount FastAPI app to Streamlit
server.get_current()._http_app.mount("/api", app)

# Streamlit UI (optional)
st.title("NameTeller API")
st.write("API is running at `/api/hello`")
st.write("You can test it by opening: [https://<your-app>.streamlit.app/api/hello](https://<your-app>.streamlit.app/api/hello)")
