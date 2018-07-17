from flask import Blueprint,request, render_template,session,redirect,url_for,request,session

from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider
from pywallet import wallet

from flask import jsonify # jsonify instad of json for resp api
#import Response #for resp api

w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))

api = Blueprint('api', __name__, 
template_folder='templates',
static_folder='static')

routePrefix = "/api/";

url = routePrefix+"generateWallet"
@api.route(url,methods = [ 'POST'])
def index():
    wordPhase = request.form.get('wordPhase')
    if(wordPhase):
        myAccount = w3.eth.account.create(wordPhase)
        myAddress = myAccount.address
        myPrivateKey = myAccount.privateKey
        publicKey = myAccount.address
        privateKey = myAccount.privateKey.hex()
        data = {
            'address'  : publicKey,
            'privateKey' : privateKey
        }
        #js = json.dumps(data)
        #resp = Response(js, status=200, mimetype='application/json')
        #resp.headers['Link'] = 'http://luisrei.com'
        return jsonify(data)
    else:
        return "a"

url = routePrefix+"getTransactions"
@api.route(url,methods = [ 'GET', 'POST'])
def getTransactions():
    blockCount = w3.eth.getBlock("latest")
    return dump(blockCount)


url = routePrefix+"sendFunds"
@api.route(url,methods = [  'POST'])
def sendFunds():
    amount = request.form.get('amount')
    privateKey = request.form.get('privateKey')
    toAddress = request.form.get('toAddress')
    gasPrice = request.form.get('gasPrice')
    if(amount and privateKey and gasPrice ):
        myAccount = w3.eth.account.create(wordPhase)


url = routePrefix+"logIn"
@api.route(url,methods = [  'POST'])
def logIn():
    address = request.form.get('address')
    passPhase = request.form.get('passPhase')
    if(passPhase and address):
        #tf = w3.personal.importRawKey(address,passPhase)
        tf = w3.personal.unlockAccount(address,passPhase,None)
    return tf

