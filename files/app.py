import uvicorn
from fastapi import FastAPI,HTTPException,Depends,Request,Body,Response,Cookie,Header
from fastapi.middleware.cors import CORSMiddleware

import city

from db.db import DB


app = FastAPI(title="Risk Control API",
    version=1.0,
    redoc_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(city.router,
    prefix="/v1",
    tags=["V1"],
    responses={404: {"description": "Not found"}})