import sys
import os
from fastapi import FastAPI
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from rootts import router

app=FastAPI()
app.include_router(router)

#cd FASTAPI_MONGO
#uvicorn main:app --reload

