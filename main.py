from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv() 

app = FastAPI() #initializes API server

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

@app.get("/")
def home():
    return {"message": "Parul Hardaha"}