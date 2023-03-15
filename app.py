from fastapi import FastAPI
import sys, os
from pymongo import MongoClient
sys.path.append(os.path.dirname((__file__)) + "/nba/")
from nbaGameLines import *
from nbaGetData import *

app = FastAPI()
client = MongoClient("mongodb+srv://shawntez32:Tezzyk32@cluster0.wpzbm.mongodb.net/?retryWrites=true&w=majority")

nba_database = client["nbaDatabase"]


@app.get("/")
def home():
    return {"Data":"Set"}

@app.get("/nba/gamelines")
def get_lines():
    return {"Data":nba_game_lines}
a = 0
@app.get("/nba/{team}/{year}")
def get_stats(team,year):
    results = []
    try:
        rec = nba_database["{}_{}".format(team,year)]
        for x in rec.find():
            del x["_id"]
            results.append(x)
        return {"Stats":results}
    except:
        data = 'wait'
        return {"Data":data}
    print(results)
