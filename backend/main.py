import uvicorn
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app=FastAPI()

@app.get("/")
def message():
    return{"message":"successful"}


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
