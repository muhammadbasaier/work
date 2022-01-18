from fastapi import APIRouter, FastAPI,HTTPException,Depends,Request,Body,Response,Cookie,Header
from db.db import DB
import json



router=APIRouter()


@router.get("/city")
def getCityDetails(Stadt_Ort:str,ID_PLZ_gesamt:int):
    db_connection =DB().connect_to_db()
    query = "SELECT ID_PLZ_gesamt,Stadt_Ort,Geo_Laenge, Geo_Breite,Hoehe WHERE Stadt_Ort LIKE %s AND ID_PLZ_gesamt LIKE %s "
    args =["%"+Stadt_Ort+"%",ID_PLZ_gesamt+"%"]
    db_connection.execute(query, args)
    result = db_connection.fetchall()
    DB().close_connection(db_connection)
    return result