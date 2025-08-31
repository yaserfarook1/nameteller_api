import streamlit as st
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.wsgi import WSGIMiddleware
from streamlit.components.v1 import html

# FastAPI app
app = FastAPI()

@app.get("/hello")
def hello():
    return JSONResponse(content={"message": "Hello Farook, what do you want?"})

# Optional: Streamlit UI
st.title("NameTeller API")
st.write("Use `/hello` endpoint to get a greeting.")

# Embed API link
st.write("[Test API](https://<your-app>.streamlit.app/hello)")
