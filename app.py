from distutils.log import debug
from logging import exception
from flask import Flask, render_template, request
import pyodbc
from azure.storage.blob import BlobServiceClient
############### 	Database connection #############
#Name	State	Salary	Grade	Room	Telnum	Picture	Keywords

server ='tcp:adbassignmentserver1.database.windows.net' 
database ='adbassignment1' 
username ='saurabh'
password ='password'
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

# Blob object for connection.
conn_blob="DefaultEndpointsProtocol=https;AccountName=storageadb01;AccountKey=ony7qoLaKWLAH7VVsndj19UxwYx93P0VKLP5Kd9YCji1hXDQsrc5rv7bFZnW7I/acOTar0O+5iRB9UK4MiFoWQ==;EndpointSuffix=core.windows.net"
container_name = "containeradb01" # container name in which images will be store in the storage account
blob_service_client = BlobServiceClient.from_connection_string(conn_str=conn_blob)
try:
    container_client = blob_service_client.get_container_client(container=container_name)
    container_client.get_container_properties()
except Exception as e:
    container_client = blob_service_client.create_container(container_name)

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world(): 	
	return render_template("home.html")

@app.route('/all')
def all_doc():
	cursor.execute("SELECT * from dbo.people;") 
	row = cursor.fetchall()
	return str(row)

@app.route("/searchname", methods=['GET','POST'])
def searchName():
    findname = str(request.args.get('searchname'))
    print(findname)
    cursor.execute("select * from dbo.people where Name = '"+ findname+ "';")
    getdata = cursor.fetchall()
    print(getdata)
    return render_template("names.html", variable=getdata[0][6] )

@app.route("/getsalary", methods=['GET','POST'])
def checkSalary():
    salary= str(request.args.get('salary'))
    cursor.execute("select Name, Salary, Picture  from dbo.people where Salary < '"+ salary +"';")
    rows = cursor.fetchall()
    newrows=[]
    for i in rows:
        if i[0] != None:
            newrows.append((i[0], i[1], i[2])   )
    return render_template("salary.html", setsalnames = rows, salary=salary)


@app.route("/viewPhoto")
def view_photos():
    return render_template("checkphoto.html")

@app.route("/picture", methods=["POST"])
def upload_photos():
    sname=(request.form["searchname"])
    filenames = ""
    for file in request.files.getlist("photos"):
        try:
            container_client.upload_blob(file.filename, file)
            filenames = file.filename
            cursor.execute("UPDATE dbo.people SET Picture = '" + filenames + "' WHERE Name='" + sname + "';")
            cursor.commit()
        except Exception as e:
            # print(e)
            print("Ignoring duplicate filenames")  # ignore duplicate filenames
    return render_template("picture.html", finalpicturename =filenames, setname = sname)

@app.route("/edit")
def changesalary():
    findname = str(request.args.get('name'))
    cursor.execute("select * from dbo.people where Name = '"+findname+"';")
    rows = cursor.fetchall()
    print(rows)
    counters=0
    if(len(rows)!=0):
        getstate = str(request.args.get('state'))
        if(getstate==''):
                getstate=str(rows[0][1])
        getsalary = str(request.args.get('salary'))
        if(getsalary==''):
            getsalary=str(rows[0][2])
        getgrade = str(request.args.get('grade'))
        if(getgrade==''):
            getgrade=str(rows[0][3])
        getroom = str(request.args.get('room'))
        if(getroom==''):
            getroom=str(rows[0][4])
        gettelnum= str(request.args.get('telnum'))
        if(gettelnum==''):
            gettelnum=str(rows[0][5])
        getkeywords= str(request.args.get('keywords'))
        if(getkeywords==''):
            getkeywords=str(rows[0][7])
        cursor.execute("UPDATE dbo.people SET State = '"+getstate+"', Salary = "+getsalary+",Grade ="+getgrade+",Room ="+getroom+",Telnum = "+gettelnum+", Keywords = '"+getkeywords+"' WHERE Name='"+findname+"';")
        cursor.commit()
        counters=1
    print(findname)
    return render_template("edit.html", counter=counters )


@app.route("/deletedata")
def deletedata():
    findname = str(request.args.get('searchname'))
    cursor.execute("select * from dbo.people where Name = '"+findname+"';")
    rows = cursor.fetchall()
    counters=0
    if(len(rows)!=0):
        cursor.execute("DELETE FROM dbo.people WHERE Name='"+findname+"';")
        cursor.commit()
        counters=1
    return render_template("deletedata.html", counter=counters)

if __name__ == '__main__':
	app.run(debug= True, port = 8000)
