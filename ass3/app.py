from flask import Flask, render_template, request
import pyodbc
from time import time
# import redis
import matplotlib.pyplot as plt, pyodbc, base64, io

server='tcp:adbass.database.windows.net'
database = 'adbdb'
username='sqladmin'
password='S@urabh9595'
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()
app =  Flask(__name__)

primary = 'kQv8CGbmCcVaFIfq3Uziom8RJbuNhevyDAzCaASW488='
# secondary = 'RtdyFGXwimiZz6erOaDQOshtzRsls0kbVAzCaAp9Blo='
# Primary_connection_string='adbass.redis.cache.windows.net:6380,password=kQv8CGbmCcVaFIfq3Uziom8RJbuNhevyDAzCaASW488=,ssl=True,abortConnect=False'

# r = redis.Redis(host='adbass.redis.cache.windows.net', port=6380,  password=primary)

@app.route('/',methods=['GET'])
def hello_world(): 	
    return render_template("home.html")
