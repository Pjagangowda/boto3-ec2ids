from logging import debug
from flask import Flask,render_template
import boto3

app=Flask(__name__)

@app.route("/jaga")
def index():
    data=boto3.resource('ec2')
    data1=data.instances.all()
    return render_template("home.html",jaga=data1)
    
if __name__=='__main__': 
    app.run(debug=True)