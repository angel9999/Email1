from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask import render_template
from flask_mail import Mail, Message
from time import localtime, strftime

import csv
import pprint
import os

app = Flask(__name__)

app.debug = True
app.secret_key = os.environ['SECRET_KEY']

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'codingbot9@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)
 
@app.route('/',methods=["POST","GET"])
def home():
    return render_template('Page1.html')
    
@app.route('/next1',methods=["POST","GET"])
def next1(): 
    
    return render_template('Page2.html')  

@app.route('/next2',methods=["POST","GET"])
def next2(): 
    session["2"] = request.form['data2']
    return render_template('Page3.html')  


@app.route('/next3',methods=["POST","GET"])
def next3(): 
    session["3"] = request.form['data3']
    return render_template('Page4.html')  
    

@app.route('/next4',methods=["POST","GET"])
def next4(): 
    session["4"] = request.form['data4']
    return render_template('Page5.html') 


@app.route('/next5',methods=["POST","GET"])
def next5(): 
    session["5"] = request.form['data5']
    return render_template('Page6.html') 

@app.route('/next6',methods=["POST","GET"])
def next6(): 
    session["6"] = request.form['data6']
    return render_template('Page7.html') 

@app.route('/end',methods=["POST","GET"])
def end(): 
    session["7"] = request.form['data7']
    
    messg ="Period 1" + ',' + "Period 2" + ',' "Period 3" + ','+ "Period 4" + ','+ "Period 5" + ',' + "Period 6" + "Date" + "\n" + session['2'] + ',' + session['3'] + ',' + session['4'] + ',' + session['5'] + ',' + session['6'] + ',' + session['7'] + ',' + strftime("%a %d %b %Y ", localtime())
    msg = Message('Hello', sender = 'codingbot9@gmail.com', recipients = ['codingbot9@gmail.com'])
    msg.attach("data.csv", "data/csv" , messg )
   
    mail.send(msg)
    return  render_template('end.html')


if __name__ == '__main__':
    os.system("echo json(array) > file")
    app.run()
