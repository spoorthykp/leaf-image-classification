from flask import Flask, render_template, request, session,make_response
import datetime
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index.html')
def inde():
    return render_template("index.html")

@app.route('/search',methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        file = request.form.get('fileupload')
        df = pd.read_csv('new.csv')
        idx = 0
        for i in df['file']:
            if file == i:
                print(i)
                x = df.iloc[idx]
                print(x['species'])
                return("<html><body><script>alert(\""+x['species']+"\");window.location.href=\"index.html\";</script></body></html>") 
            idx+=1
        return("<html><body><script>alert(\"That Species Of Leaf is Not Added To CNN\");window.location.href=\"index.html\";</script></body></html>") 
          
if __name__ == '__main__':
    app.run(debug=True)
