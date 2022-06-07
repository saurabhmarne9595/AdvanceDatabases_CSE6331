from code import interact
from distutils.log import error
from  flask import Flask, redirect, render_template, request
import matplotlib.pyplot as plt, pyodbc, base64, io

server_name = 'marneserver'
server = '{server_name}.database.windows.net,1433;'.format(server_name=server_name)
database = 'marnedb'
username = 'marneadmin'
password = 'my_password'
# Connection_str="Driver={ODBC Driver 17 for SQL Server};Server=tcp:adbass.database.windows.net,1433;Database=adbdb;Uid=sqladmin;Pwd=my_password;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"        
Connection_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
app = Flask(__name__)
conn = pyodbc.connect(Connection_str)
cursor=conn.cursor()

@app.route('/',methods=['GET'])
def hello_world(): 	
    return render_template("home.html")

# #q1
# @app.route('/fquestion1', methods=['GET','POST'])
# def fquestion1():
#     if request.method=='POST':
#         return redirect('lquestion1.html')  
#     return render_template('fquestion1.html')

# @app.route('/lquestion1', methods=['GET','POST'])
# def lquestion1():
#     fig = plt.figure(1, figsize=(10, 4))
#     getmag = str(request.form.get('magnitude'))
#     cursor.execute("select count(*) from dbo.all_month_ass4 where mag>= "+getmag+" ;")
#     quakes=cursor.fetchall()[0][0]
#     cursor.execute("select count(*) from dbo.all_month_ass4;")
#     totalquakes=cursor.fetchall()[0][0]
#     print(cursor)
#     print(totalquakes)
#     size=[quakes,totalquakes-quakes]
#     chart=fig.add_subplot(111)
#     explode=[0,0.1]
#     labels="Earthquakes where magnitude >="+getmag+"","Earhtquakes where magnitude<"+getmag+""
#     chart.pie(size, labels=labels, explode=explode, wedgeprops={'edgecolor':'black'}, autopct='%1.1f%%')
#     imgage = io.BytesIO()
#     plt.savefig(imgage, format='png')
#     imgage.seek(0)
#     plot_url= base64.b64encode(imgage.getvalue()).decode()
#     plt.clf()
#     chart.cla()
#     return render_template('lquestion1.html', pieimage=plot_url)

# #q2
# @app.route('/fquestion2', methods=['GET','POST'])
# def fquestion2():
#     if request.method=='POST':
#         return redirect('lquestion2.html') 
#     return render_template('fquestion2.html')

# @app.route('/lquestion2', methods=['GET','POST'])
# def lquestion2():
#     fig = plt.figure(1, figsize=(10, 4))
#     getminmag = str(request.form.get('firstmagnitude'))
#     getmaxmag = str(request.form.get('lastmagnitude'))
#     getmindate = str(request.form.get('firstdate'))
#     getmindate=getmindate
#     getmaxdate = str(request.form.get('lastdate'))
#     getmaxdate=getmaxdate
#     print(getmaxdate)
#     print(type(getmaxdate))
#     getdata=[]
#     magnitudes = []
#     for i in range(int(getminmag), (int(getmaxmag)+1)):
#         cursor.execute("select count(*) from dbo.all_month_ass4 where mag="+str(i)+" AND time>='"+getmindate+"' AND time<='"+getmaxdate+"';")
#         getdata.append(cursor.fetchall()[0][0])
#         magnitudes.append(i)
#     chart = fig.add_subplot(111)
#     magnitudelabels = [str(getminmag)+'-'+str(getmaxmag)]
#     width = 0.2
#     chart.bar(magnitudes, getdata, color='#5a7d9a', linewidth=1.5, width=width, label ='Earthquake Count')
#     plt.xlabel('Magnitudes')
#     plt.ylabel('Total Number of Earthquakes')
#     plt.title('BAR CHART')
#     plt.legend()
#     imgage = io.BytesIO()
#     plt.savefig(imgage, format='png')
#     imgage.seek(0)
#     plot_url= base64.b64encode(imgage.getvalue()).decode()
#     plt.clf()
#     chart.cla()
#     return render_template('lquestion2.html',barimage=plot_url)

# #q3
# @app.route('/fquestion3', methods=['GET','POST'])
# def fquestion3():
#     if request.method=='POST':
#         return redirect('lquestion3.html') 
#     return render_template('fquestion3.html')

# @app.route('/lquestion3', methods=['GET','POST'])
# def lquestion3():
#     fig = plt.figure(1, figsize=(10, 4))
#     getlongitude = str(request.form.get('longi'))
#     getlatitude = str(request.form.get('lati'))
#     getsurrounding = str(request.form.get('surrounding'))
#     leftlatitude=float(getlatitude) - float(getsurrounding)/111
#     rightlatitude=float(getlatitude) + float(getsurrounding)/111
#     bottomlongitude=float(getlongitude) - float(getsurrounding)/111
#     toplongitude=float(getlongitude) + float(getsurrounding)/111
#     cursor.execute("select count(*) from dbo.all_month_ass4 where (latitude>= "+str(leftlatitude)+" AND latitude<= "+str(rightlatitude)+" ) AND ( longitude>= "+str(bottomlongitude)+" AND longitude<= "+str(toplongitude)+");")
#     getdata = cursor.fetchall()[0][0]
#     cursor.execute("select count(*) from dbo.all_month_ass4;")
#     totalquakes=cursor.fetchall()[0][0]
#     size=[getdata,totalquakes-getdata]
#     chart=fig.add_subplot(111)
#     explode=[0,0.1]
#     labels="Earthquakes within the range","Earhtquakes that are not within the range"
#     chart.pie(size, labels=labels, explode=explode, wedgeprops={'edgecolor':'black'}, autopct='%1.1f%%')
#     imgage = io.BytesIO()
#     plt.savefig(imgage, format='png')
#     imgage.seek(0)
#     plot_url= base64.b64encode(imgage.getvalue()).decode()
#     plt.clf()
#     chart.cla()
#     return render_template('lquestion3.html', pieimage=plot_url)

# #q4
# @app.route('/fquestion4', methods=['GET','POST'])
# def fquestion4():
#     if request.method=='POST':
#         return redirect('lquestion4.html') 
#     return render_template('fquestion4.html')

# @app.route('/lquestion4', methods=['GET','POST'])
# def lquestion4():
#     fig = plt.figure(1, figsize=(10, 4))
#     getmag = str(request.form.get('magnitude'))
#     getdata=[]
#     magnitudes = []
#     for i in range(int(getmag)):
#         i=i+1
#         magnitudes.append(i)
#         cursor.execute("select count(*) from dbo.all_month_ass4 where mag="+str(i)+";")
#         getdata.append(cursor.fetchall()[0][0])

#     chart = fig.add_subplot(111)
    
#     width = 0.2
#     chart.bar(magnitudes, getdata, color='#5a7d9a', linewidth=1.5, width=width)
#     plt.xlabel('Magnitudes')
#     plt.ylabel('Total Number of Earthquakes')
#     plt.title('BAR CHART')
#     plt.legend()
#     imgage = io.BytesIO()
#     plt.savefig(imgage, format='png')
#     imgage.seek(0)
#     plot_url= base64.b64encode(imgage.getvalue()).decode()
#     plt.clf()
#     chart.cla()
#     return render_template('lquestion4.html', barimage=plot_url)

# #q5
# @app.route('/fquestion5', methods=['GET','POST'])
# def fquestion5():
#    if request.method=='POST':
#         return redirect('lquestion5.html') 
#    return render_template('fquestion5.html')

# @app.route('/lquestion5', methods=['GET','POST'])
# def lquestion5():
#     fig = plt.figure(1, figsize=(10, 4))
#     quakes=[]
#     cursor.execute("select count(*) from dbo.all_month_ass4 where mag<1;")
#     quakes.append(cursor.fetchall()[0][0])
#     cursor.execute("select count(*) from dbo.all_month_ass4 where mag>=1 and mag<=2;")
#     quakes.append(cursor.fetchall()[0][0])
#     cursor.execute("select count(*) from dbo.all_month_ass4 where mag>2 and mag<=3;")
#     quakes.append(cursor.fetchall()[0][0])
#     cursor.execute("select count(*) from dbo.all_month_ass4 where mag>3 and mag<=4;")
#     quakes.append(cursor.fetchall()[0][0])
#     cursor.execute("select count(*) from dbo.all_month_ass4 where mag>4 and mag<=5;")
#     quakes.append(cursor.fetchall()[0][0])
#     size=quakes
#     chart=fig.add_subplot(111)
#     explode=[0, 0, 0, 0, 0]
#     labels='magnitude less than 1','magnitude between 1 and 2','magnitude between 2 and 3','magnitude between 3 and 4','magnitude between 4 and 5'
#     chart.pie(size, labels=labels, explode=explode, wedgeprops={'edgecolor':'black'}, autopct='%1.1f%%')
#     imgage = io.BytesIO()
#     plt.savefig(imgage, format='png')
#     imgage.seek(0)
#     plot_url= base64.b64encode(imgage.getvalue()).decode()
#     plt.clf()
#     chart.cla()
#     return render_template('lquestion5.html', pieimage=plot_url)


# #q6
# @app.route('/fquestion6', methods=['GET','POST'])
# def fquestion6():
#     if request.method=='POST':
#         return redirect('lquestion6.html') 
#     return render_template('fquestion6.html')

# @app.route('/lquestion6', methods=['GET','POST'])
# def lquestion6():
#     fig = plt.figure(1, figsize=(10, 4))
#     magnitude=[]
#     deptherror=[]
#     cursor.execute("select top 100 mag,depthError from dbo.all_month_ass4 order by time desc;")
#     data= cursor.fetchall()
#     for i in range(len(data)):
#         magnitude.append(data[i][0])
#         deptherror.append(data[i][1])
#     chart=fig.add_subplot(111)
#     chart.scatter(magnitude, deptherror, color='b')
#     chart.set_xlabel('Magnitude')
#     chart.set_ylabel('Depth Error')
#     chart.set_title('Scatter Chart')
#     image = io.BytesIO()
#     plt.savefig(image, format='png')
#     image.seek(0)
#     plot_url= base64.b64encode(image.getvalue()).decode()
#     plt.clf()
#     chart.cla()
#     return render_template('lquestion6.html', scatterimage=plot_url)




@app.route('/quiz4_5', methods=['GET','POST'])
def quiz4_5():
    if request.method=='POST':
        return redirect('quiz4_5_a.html') 
    return render_template('quiz4_5.html')

@app.route('/quiz4_5_a', methods=['GET','POST'])
def quiz4_5_a():
    fig = plt.figure(1, figsize=(10, 4))
    getN = str(request.form.get('N'))
    num_slices = int(getN)
    interval = (211-8)/num_slices
    data_N = []
    range_start = 8
    labels = []
    for i in range(int(getN)):
        cursor.execute("select count(column3) from dbo.quiz4 where column3 between "+ str(range_start)+ " and "+ str(range_start+interval) +" ;")
        getdata = cursor.fetchall()[0][0]
        temp_label = "range from "+str(range_start)+ " to "+ str(range_start+interval)
        range_start+=interval
        data_N.append(getdata)
        labels.append(temp_label)

    chart=fig.add_subplot(111)
    chart.pie(data_N, labels=labels,  wedgeprops={'edgecolor':'black'}, autopct='%1.1f%%')
    imgage = io.BytesIO()
    plt.savefig(imgage, format='png')
    imgage.seek(0)
    plot_url= base64.b64encode(imgage.getvalue()).decode()
    plt.clf()
    chart.cla()

    return render_template('quiz4_5_a.html', pieimage=plot_url)




#Quiestion 6
@app.route('/quiz4_6', methods=['GET','POST'])
def quiz4_6():
    if request.method=='POST':
        return redirect('quiz4_6_a.html') 
    return render_template('quiz4_6.html')

@app.route('/quiz4_6_a', methods=['GET','POST'])
def quiz4_6_a():
    fig = plt.figure(1, figsize=(10, 4))
    rangehigh = str(request.form.get('rangehigh'))
    rangelow = str(request.form.get('rangelow'))
    getN = str(request.form.get('N'))
    num_slices = int(getN)
    print(rangelow)
    print(rangehigh)
    print(num_slices)
    interval = (int(rangehigh)-int(rangelow))/num_slices
    data_N = []
    range_start = int(rangelow)
    labels = []
    for i in range(int(getN)):
        cursor.execute("select count(column3) from dbo.quiz4 where column3 between "+ str(range_start)+ " and "+ str(range_start+interval) +" ;")
        getdata = cursor.fetchall()[0][0]
        temp_label = str(range_start)+ "-"+ str(range_start+interval)
        range_start+=interval
        data_N.append(getdata)
        labels.append(temp_label)
    chart = fig.add_subplot(111)
    print(data_N)
    print(labels)
    width = 0.4
    chart.bar(labels, data_N, color='#5a7d9a', linewidth=1.5, width=width, label ='range Count')
    plt.xlabel('Magnitudes')
    plt.ylabel('Total Number of Earthquakes')
    plt.title('BAR CHART')
    plt.legend()
    imgage = io.BytesIO()
    plt.savefig(imgage, format='png')
    imgage.seek(0)
    plot_url= base64.b64encode(imgage.getvalue()).decode()
    plt.clf()
    chart.cla()
    return render_template('quiz4_6_a.html',barimage=plot_url)

#question 7 
@app.route('/quiz4_7', methods=['GET','POST'])
def quiz4_7():
    if request.method=='POST':
        return redirect('quiz4_7_a.html') 
    return render_template('quiz4_7.html')

@app.route('/quiz4_7_a', methods=['GET','POST'])
def quiz4_7_a():
    rangehigh = str(request.form.get('rangehigh'))
    rangelow = str(request.form.get('rangelow'))
    getN = str(request.form.get('N'))
    fig = plt.figure(1, figsize=(10, 4))
    cursor.execute("select column3 from dbo.quiz4 between "+ str(rangelow) + " and "+ str(rangehigh)+ ";")
    data_col3= cursor.fetchall()
    cursor.execute("select column2 from dbo.quiz4;")
    data_col2= cursor.fetchall()
    cursor.execute("select column1 from dbo.quiz4;")
    data_col1= cursor.fetchall()

    
    print(data_col3)
    # for i in range(len(data_col3)):
        # magnitude.append(data[i][0])
        # deptherror.append(data[i][1])
    chart=fig.add_subplot(111)
    chart.scatter(data_col1, data_col3, color='b')
    chart.set_xlabel('Magnitude')
    chart.set_ylabel('Depth Error')
    chart.set_title('Scatter Chart')
    image = io.BytesIO()
    plt.savefig(image, format='png')
    image.seek(0)
    plot_url= base64.b64encode(image.getvalue()).decode()
    plt.clf()
    chart.cla()
    return render_template('lquestion6.html', scatterimage=plot_url)



if __name__ == '__main__':
    app.run(debug= True, port = 8000)
