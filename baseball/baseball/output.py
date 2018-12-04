#!/usr/bin/env python

import pymongo
from pymongo import MongoClient
from pprint import pprint
import json
try: 
    conn = MongoClient('mongodb://localhost:27017/') 
    #print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 
  
# database name: mydatabase 
db = conn.baseball
  
# Created or Switched to collection names: myTable 
collection = db.team_stats 
  
# To find() all the entries inside collection name 'myTable' 
cursor = collection.find() 

print("<table class='stats-table table table-hover table-dark table-sm'><th scope='col'>Team</th><th scope='col'>AB</th><th scope='col'>BA</th><th scope='col'>BB</th><th scope='col'>CS</th><th scope='col'>GDP</th><th scope='col'>HBP</th><th scope='col'>HR</th><th scope='col'>LOB</th><th scope='col'>OBP</th><th scope='col'>OPS</th><th scope='col'>OPSP</th><th scope='col'>PA</th><th scope='col'>RBI</th><th scope='col'>SB</th><th scope='col'>SF</th><th scope='col'>SH</th><th scope='col'>SLG</th><th scope='col'>SO</th><th scope='col'>TB</th><th scope='col'>Average Bat Age</th><th scope='col'>Doubles</th><th scope='col'>Games</th><th scope='col'>Hits</th><th scope='col'>Runs</th><th scope='col'>Runs per Game</th><th scope='col'>Triples</th>")

for item in cursor:
    #print("<tr>"+item["team"])
    print("<tr scope='row'>")
    print("<td>")
    print(u", ".join(item["team"]) )  #.encode('ascii', 'ignore') )
    print("</td>")

    print("<td>")
    print(u", ".join(item["AB"]))
    print("</td>")

    print("<td>")
    print u", ".join(item["BA"])
    print("</td>")

    print("<td>")
    print u", ".join(item["BB"])
    print("</td>")

    print("<td>")
    print u", ".join(item["CS"])
    print("</td>")

    print("<td>")
    print u", ".join(item["GDP"])
    print("</td>")

    print("<td>")
    print u", ".join(item["HBP"])
    print("</td>")

    print("<td>")
    print u", ".join(item["HR"])
    print("</td>")

    print("<td>")
    print u", ".join(item["LOB"])
    print("</td>")

    print("<td>")
    print u", ".join(item["OBP"])
    print("</td>")

    print("<td>")
    print u", ".join(item["OPS"])
    print("</td>")

    print("<td>")
    print u", ".join(item["OPSP"])
    print("</td>")

    print("<td>")
    print u", ".join(item["PA"])
    print("</td>")

    print("<td>")
    print u", ".join(item["RBI"])
    print("</td>")

    print("<td>")
    print u", ".join(item["SB"])
    print("</td>")

    print("<td>")
    print u", ".join(item["SF"])
    print("</td>")

    print("<td>")
    print u", ".join(item["SH"])
    print("</td>")

    print("<td>")
    print u", ".join(item["SLG"])
    print("</td>")

    print("<td>")
    print u", ".join(item["SO"])
    print("</td>")

    print("<td>")
    print u", ".join(item["TB"])
    print("</td>")


    print("<td>")
    print u", ".join(item["average_bat_age"])
    print("</td>")

    print("<td>")
    print u", ".join(item["doubles"])
    print("</td>")

    print("<td>")
    print u", ".join(item["games"])
    print("</td>")

    print("<td>")
    print u", ".join(item["hits"])
    print("</td>")

    print("<td>")
    print u", ".join(item["runs"])
    print("</td>")

    print("<td>")
    print u", ".join(item["runs_per_game"])
    print("</td>")

    print("<td>")
    print u", ".join(item["triples"])
    print("</td>")

    #print(item.split(';'))
    print("</tr>")

print("</table>")

#return cursor
