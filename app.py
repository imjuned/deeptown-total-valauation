
from flask import Flask
from flask import render_template,request,redirect,url_for

app = Flask(__name__)


@app.route('/')
def login():
    print("hello")
    return render_template('index.html')







if __name__=='__main__':
    app.run(debug=True)