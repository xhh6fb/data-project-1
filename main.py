from fastapi import FastAPI
#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import mysql.connector
import os

api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello API"}

@api.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    return {"result": a + b}

@api.get('/genres')
def get_genres():
    query = "SELECT * FROM genres ORDER BY genreid;"
    try:    
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        return(json_data)
    except Error as e:
        print("MySQL Error: ", str(e))
        return None
    cur.close()

@api.get('/songs')
def get_songs():
    query = """
    SELECT 
        songs.title, 
        songs.album, 
        songs.artist, 
        songs.year, 
        songs.file, 
        songs.image, 
        genres.genre
    FROM songs
    JOIN genres ON songs.genre = genres.genreid
    ORDER BY songs.title;
    """
    try:
        cur = db.cursor()
        cur.execute(query)        
        headers = [x[0] for x in cur.description]
        results = cur.fetchall()
        json_data = []
        
        # Convert each row into a dictionary
        for result in results:
            json_data.append(dict(zip(headers, result)))
        
        return json_data
    except Error as e:
        print("MySQL Error: ", str(e))
        return None
    cur.close()

DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')
DB = "xhh6fb"

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()
