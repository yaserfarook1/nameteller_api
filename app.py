import streamlit as st
import json

st.set_page_config(page_title="NameTeller API", page_icon="👋")

# Hide Streamlit UI (so it feels like a pure API)
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Our "endpoint"
path = st.experimental_get_query_params().get("path", [""])[0]

if path == "hello":
    st.json({"message": "Hello Farook, what do you want?"})
else:
    st.json({"status": "ok"})
