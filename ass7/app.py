# from code import interact
# from distutils.log import error
from  flask import Flask, render_template, request, redirect
import pyodbc
server_name = 'marneserver'
server = '{server_name}.database.windows.net,1433;'.format(server_name=server_name)
database = 'marnedb'
username = 'marneadmin'
password = 'my_password'
Connection_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
app = Flask(__name__)
conn = pyodbc.connect(Connection_str)
cursor=conn.cursor()

# primary = '----------------------------------='
# secondary = '------------------------------='
# Primary_connection_string='adbass.redis.cache.windows.net:6380,password=----------------------------------=,ssl=True,abortConnect=False'

# r = redis.Redis(host='adbass.redis.cache.windows.net', port=6380,  password=primary)

@app.route('/',methods=['GET'])
def hello_world(): 	
    return "home.html"

# @app.route('/customquery', methods = ['GET'])
# def customQuery():
#     query = str(request.args.get('query'))
#     print(query)

#     cursor.execute(query)
#     getdata = cursor.fetchall()
#     return render_template('customquery.html', rows = getdata)

@app.route('/caquakes', methods = ['GET'])
def caQuery():
    query = "select * from ni;"
    cursor.execute(query)
    getdata = cursor.fetchall()
    # print(getdata)
    # for i in getdata:
        # print(i[0], i[1])
    return render_template('a1.html', rows = getdata)

# @app.route('/q1', methods=['GET','POST'])
# def quiz4_7():
#     if request.method=='POST':
#         return redirect('quiz4_7_a.html') 
#     return render_template('quiz4_7.html')

# @app.route('/q1a', methods=['GET','POST'])
# def quiz4_7_a():
#     rangehigh = str(request.form.get('rangehigh'))
#     rangelow = str(request.form.get('rangelow'))
#     cursor.execute("select column3 from dbo.quiz4 between "+ str(rangelow) + " and "+ str(rangehigh)+ ";")    data_col3= cursor.fetchall()
#     cursor.execute("select column2 from dbo.quiz4;")
#     cursor.execute("select column1 from dbo.quiz4;")
#     getdata = cursor.fetchall()
#     return render_template('a1.html', rows = getdata)





if __name__ == '__main__':
    app.run(debug= True, port = 8000)
