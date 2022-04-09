from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '66294800a89b651b6fb0293af3823f76'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# routes.py先导入了app,所以route导入要在app后边
from flaskblog import routes