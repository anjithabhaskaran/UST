from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS
from flaskext.mysql import MySQL
from flask_jwt_extended import JWTManager

mydb = MySQL()
# Create a Flask application instance
app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS) for the app
CORS(app)

# MySQL database configuration
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
# app.config['MYSQL_DATABASE_DB'] = 'carbonfootprint'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# Configure the SQLAlchemy database connection
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/carbonfootprint'

# # #  PRODUCTION config.py
# # # Azure MySQL details
# azure configuration
app.config['MYSQL_DATABASE_USER'] = 'esgUser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'User_123'
app.config['MYSQL_DATABASE_DB'] = 'carbonfootprint'
app.config['MYSQL_DATABASE_HOST'] = 'esgservernew.mysql.database.azure.com'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://esgUser:User_123@esgservernew.mysql.database.azure.com/carbonfootprint?ssl_ca=DigiCertGlobalRootCA.crt.pem"

app.config['JWT_SECRET_KEY'] = '4963cf9d82bb49849dfbd93bfb80bd88'
# Create a SQLAlchemy database instance
db = SQLAlchemy(app)
mydb.init_app(app)
jwt = JWTManager(app)
