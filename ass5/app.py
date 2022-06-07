#  app.py  env  templates  use.txt  use02.txt  use02_pre.txt  use03.txt  use03_pre.txt  use_pre.txt
# from email.mime import app
from  flask import Flask, redirect, render_template, request
import os, regex as re, string
import nltk
nltk.download('/punkt')
nltk.download('/stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords



app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world(): 	
	return "home.html"

#Pre-Processing the file

@app.route('/quiz5_q1', methods=['GET','POST'])
def quiz5_q1():
    if request.method=='POST':
        return redirect('quiz5_a1.html') 
    return render_template('quiz5_q1.html')

@app.route("/quiz5_a1",methods=['GET','POST'])
def quiz5_a1():
    for file in os.listdir():
        # print(file)
        if(file.endswith('.txt') and not file.endswith('_pre.txt')):
            filepath=f"{file}"
            print(filepath)
            filepathout=file.split(".")[0]+"_pre.txt"
            fh=open(filepath,"r", encoding="utf8")
            fo=open(filepathout,"w", encoding="utf8")
            s=" "
            while(s):
                s=fh.readline()
                if not(s.strip()=="" or s=="\n" or s=="\r"):
                    s=s.lower()
                    s=re.sub(r"\d+","",s)
                    s=s.ls("")
                    s=s.translate(str.maketrans("","",string.punctuation))
                    s=s.replace("''","")
                    stop_words=set(stopwords.words("english"))
                    tokens=word_tokenize(s)
                    result=[i for i in tokens if not i in stop_words]
                    result=[word for word in result if word.isalpha()]
                    k=""
                    for i in result:
                        k=k+" "+i
                    k=k+"\n"
                    fo.writelines(k)
                else:
                    fo.writelines(s)
            fo.close()
            fh.close()
            haa=open("pg67775_pre.txt")
            readd = haa.read()
            for i in range(0,100):
                print(readd[i])
            
    return render_template("quiz5_a1.html")




#Getting input from user and searching the text in the txt files
@app.route('/quiz5_q2', methods=['GET','POST'])
def quiz5_q2():
    if request.method=='POST':
        return redirect('quiz5_a2.html') 
    return render_template('quiz5_q2.html')

@app.route("/quiz5_a2", methods=['GET','POST'])
def quiz5_a2():
    getwordas = str(request.form.get('word'))
    getword = getwordas.lower()
    num = 0
    searchedtextresults =[]
    for file in os.listdir():
      if not file.endswith('_pre.txt'):
          continue  
      fh=open(file,"r", encoding="utf8", errors='ignore')
    #   print(fh)
      pfile = file.split("_pre")[0]+".txt"
    #   print(pfile)
      fh2=open(pfile,"r", encoding="utf8", errors='ignore')
    #   print(fh2)
    #   print("-----> file: ",pfile)
      s=" "
      count=1
      while(s):
        s=fh.readline()
        s2=fh2.readline()
        L2=s2.split()
        if getword in s:
           searchedtextresults.append([count,L2,pfile,getword,s2])
           num+=1
        count+=1
      fh.close()
    return render_template('quiz5_a2.html', textsearchlist = searchedtextresults, num = num)

#hyperlink
#Getting input from user and searching the text in the txt files
@app.route('/quiz5_q3', methods=['GET','POST'])
def quiz5_q3():
    if request.method=='POST':
        return redirect('quiz5_a3.html') 
    return render_template('quiz5_q3.html')


@app.route("/selectanddisplay", methods=['GET','POST'])
def quiz5_a3():
    getfilename=str(request.form.get("textfilename"))
    # getlinenumber=str(request.args.get("linenumber"))
    getline=str(request.form.get("line"))
    filepath=f"{getfilename}"
    
    fh=open(filepath,"r",encoding="utf8")
    textlines=list(fh)
    fh.close()
    #linenum=getlinenumber,
    return render_template("quiz5_a3.html",alltextlines=textlines, setline=getline)


@app.route('/q1', methods=['GET','POST'])
def q1():
    if request.method=='POST':
        return redirect('a1.html') 
    return render_template('q1.html')

@app.route("/a1",methods=['GET','POST'])
def a1():
    filepath = "text.txt"
    filepathout = "./text_pre.txt"
    print(filepath)
    fh=open(filepath,"r", encoding="utf8")
    fo=open(filepathout,"w", encoding="utf8")
    s=" "
    while(s):
        s=fh.readline()
        if not(s.strip()=="" or s=="\n" or s=="\r"):
            s=s.lower()
            s=re.sub(r"\d+","",s)
            s=s.ls("")
            s=s.translate(str.maketrans("","",string.punctuation))
            s=s.replace("''","")
            stop_words=set(stopwords.words("english"))
            tokens=word_tokenize(s)
            result=[i for i in tokens if not i in stop_words]
            result=[word for word in result if word.isalpha()]
            k=""
            for i in result:
                k=k+" "+i
            k=k+"\n"
            fo.writelines(k)
        else:
            fo.writelines(s)
    fo.close()
    fh.close()
    return render_template("q1.html")




if __name__ == '__main__':
    app.run(debug= True, port = 8000)
