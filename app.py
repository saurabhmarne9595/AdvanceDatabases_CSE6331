from distutils.log import debug
from logging import exception
from flask import Flask, render_template, request
import pyodbc
from azure.storage.blob import BlobServiceClient
############### 	Database connection #############

server ='tcp:adbassignmentserver1.database.windows.net' 
database ='adbassignment1' 
username ='saurabh'
password ='my_password'
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def hello_world(): 	
    query="SELECT TOP (5) * FROM [dbo].[ass2_all_month]"
    cursor.execute(query) 
    row = cursor.fetchall()
    return render_template('home.html', variable=row)

@app.route('/largest',methods=['GET','POST'])
def largest(): 	
    findN=str(request.args.get('n'))
    '''     select * from dbo.ass2_all_month where ( mag IN (
                SELECT top 5 mag FROM dbo.ass2_all_month as table1 group by mag order by mag desc )    );
    '''
    query="select * from dbo.ass2_all_month where ( mag IN ( SELECT top "+ findN +" mag FROM dbo.ass2_all_month as table1 group by mag order by mag desc));"
    cursor.execute(query) 
    rows = cursor.fetchall()
    return render_template('largest.html', rows=rows)

@app.route('/nearArlington',methods=['GET','POST'])
def nearArlington(): 	
    # findN=str(request.args.get('n'))
    '''     select * from dbo.ass2_all_month where ( mag IN (
                SELECT top 5 mag FROM dbo.ass2_all_month as table1 group by mag order by mag desc )    );
        32.7357° N, 97.1081° W
        32.729641, -97.110566
        select * from dbo.ass2_all_month where longitude BETWEEN  44.729641 and 20.229641 ;
    '''
    query= "SELECT longitude, latitude, place, [time] FROM dbo.ass2_all_month WHERE longitude BETWEEN '-110' AND '-89' AND latitude BETWEEN  '23' and '49';"
    cursor.execute(query) 
    rows = cursor.fetchall()
    return render_template('nearArlington.html', rows=rows)

@app.route('/recentRange',methods=['GET','POST'])
def recentRange(): 	
    getmindate = str(request.args.get('firstdate'))
    getmaxdate = str(request.args.get('lastdate'))
    print(getmaxdate)
    print(getmindate)
    query = " select top 20 t.blah as [score range], count(*) as [number of occurences] from ( select case when mag between  1 and  2 then ' 1-2 ' when mag between  2 and  3 then ' 2-3 ' when mag between  3 and  4 then ' 3-4 ' when mag between  3 and  4 then ' 4-5 ' when mag between  5 and  6 then ' 5-6 '  when mag between  6 and  7 then ' 6-7 '  else '8-above' end as blah from ass2_all_month where time>='"+getmindate+' "AND time<= ' + getmaxdate + "') t group by t.blah ;"
    cursor.execute(query) 
    rows = cursor.fetchall()
    return render_template('recentRange.html', rows=rows)

# count of the quaakes betwwen given range: SELECT COUNT(id) from ass2_all_month where mag BETWEEN 1 and 2; 
# SELECT * FROM [dbo].[all_months] WHERE TIME BETWEEN '2022-01-20 00:00:00.000' AND '2022-01-26 23:59:59.000' AND mag > 3
#SELECT longitude, latitude, place, [time] FROM dbo.ass2_all_month WHERE longitude BETWEEN '-99' AND '-93' AND latitude BETWEEN  '32' and '39';

@app.route('/anchorage',methods=['GET','POST'])
def anchorage(): 	
    getlongitude = str(request.form.get('longi'))
    getlatitude = str(request.form.get('lati'))
    getsurrounding = str(request.form.get('surrounding'))
    leftlatitude=float(getlatitude) - float(getsurrounding)/111
    rightlatitude=float(getlatitude) + float(getsurrounding)/111
    bottomlongitude=float(getlongitude) - float(getsurrounding)/111
    toplongitude=float(getlongitude) + float(getsurrounding)/111
    cursor.execute("select top 1 mag, place, time, latitude, longitude from dbo.all_month where (latitude>= "+str(leftlatitude)+" AND latitude<= "+str(rightlatitude)+" ) AND ( longitude>= "+str(bottomlongitude)+" AND longitude<= "+str(toplongitude)+") order by mag desc ;")
    rows = cursor.fetchall()
    return render_template('anchorage.html', rows=rows)
    

#################################### quiz 2
@app.route('/q10',methods=['GET','POST'])
def q10(): 	
    getlat = str(request.args.get('latitude'))
    getdeg = str(request.args.get('degrees'))
    lat2 = str(int(getlat)+ int(getdeg))
    lat1 = str(int(getlat)- int(getdeg))
    query = " SELECT time, latitude, longitude, id,  place from eq where latitude between "+  lat1+" and "+ lat2+";"
    cursor.execute(query) 
    rows = cursor.fetchall()
    return render_template('q10.html', rows=rows)

@app.route('/q12',methods=['GET','POST'])
def q12(): 	
    getmaxmag = str(request.args.get('maxmag'))
    getminmag = str(request.args.get('minmag'))
    getplace = str(request.args.get('place'))
    query = "SELECT time, latitude, longitude, mag, place from eq where  place LIKE '%"+getplace+"%' and mag between "+ getminmag +" and "+getmaxmag+   ";"
    cursor.execute(query) 
    rows = cursor.fetchall()
    return render_template('q12.html', rows=rows)

@app.route('/q11',methods=['GET','POST'])
def q11(): 	
    getn = str(request.args.get('n'))
    getnet = str(request.args.get('net'))
    getsamll = str(request.args.get('smalln'))
    getlarge = str(request.args.get('largen'))
    query = "UPDATE eq SET gap = "+ getn + " WHERE net = '"+ getnet+"';"
    cursor.execute(query) 
    #        select count(id) from eq where gap BETWEEN 1 and 3;
    query = "select count(id) from eq WHERE gap between "+getsamll +" and "+ getlarge +" then;"
    cursor.execute(query) 
    rows = cursor.fetchall()
    return render_template('q11.html',rows=rows)

if __name__ == '__main__':
	app.run(debug= True, port = 8000)

