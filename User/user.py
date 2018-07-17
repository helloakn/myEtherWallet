from flask import Blueprint,render_template,session,redirect,url_for,request
import sys
#from config.dbConnect import dbConnect
#from config.db import db


user = Blueprint('user', __name__, 
template_folder='templates',
static_folder='static')

@user.route('/',methods = [ 'GET'])
def index():
    session['privateKey'] = "hello"
    
    return render_template('getBalance.html') 

@user.route('/checkTransaction',methods = [ 'GET','POST'])
def checkTransaction():
    privateKey = session['privateKey']
    address = session['address']
    return render_template('checkTransaction.html',privateKey=privateKey,address=address) 

@user.route('/sendFunds',methods = [ 'GET','POST'])
def sendFunds():
    privateKey = session['privateKey']
    
    return render_template('sendFunds.html',privateKey=privateKey,pageName="Send Funds to Friends") 

@user.route('/getTransaction',methods = [ 'GET','POST'])
def getTransaction():
    privateKey = session['privateKey']
    
    return render_template('getTransaction.html',privateKey=privateKey,pageName="Transactions List") 
