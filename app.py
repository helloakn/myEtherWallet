from flask import Flask, render_template #,session
#from flask.ext.session import Session



from flaskext.mysql import MySQL
mysql = MySQL()

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)     

#Session(app)            

from User.user import user
app.register_blueprint(user) 
from API.api import api
app.register_blueprint(api) 
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0',port=90,debug = True)
   