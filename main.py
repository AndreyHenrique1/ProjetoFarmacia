from flask import Flask

from database.db import db
from routes.routeIndex import routeIndex

class MyServer():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/farmacia'
        db.init_app(self.app)
        routeIndex(self.app)

    def run(self):
        self.app.run(port=3000, debug=True, host="localhost")
    
    

app = MyServer()
app.run()