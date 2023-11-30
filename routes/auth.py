from services.logger import logger
from flask import jsonify, request
from flask_restx import Api, Resource, fields, Namespace
from model.emission import User
from configs.config import db, app 
import pymysql
import bcrypt
from datetime import datetime, timedelta
import jwt

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Configure the Flask-RESTx API
# Create a namespace for login operations
login_name_space = Namespace('login', description='login operations')

# Define the data model for login
login_emission_model = login_name_space.model('LoginEmissionModel', {
    'username':fields.String(required=True),
    'password':fields.String(required=True)
})

# Create an endpoint for handling Fugitive Emissions
@login_name_space.route('')
class Login(Resource):
    @login_name_space.expect(login_emission_model)
    def post(self):
 
        try:
            json_data = request.json
            user_name = json_data['username']
            password = json_data['password']
            user = User.query.filter_by(user_name=user_name).first()
            print("kkk")
            print(user)
            hashed_password = user.password
            user_id = user.user_id
            print("------hashed_password-----",hashed_password)
            if ( bcrypt.checkpw(password.encode('utf-8'),hashed_password.encode('utf-8'))):
                access_token = jwt.encode(
                    {'user_id': user_id,
                    'expiration': str(datetime.utcnow() + timedelta(minutes=30))},
                    app.config['JWT_SECRET_KEY'])
                print("--------access_token________",access_token)
                return jsonify(
                    message='Login Successful',
                    access_token=access_token,
                )
                
            else :
                return jsonify(error='Username or Password is incorrect, Try with the correct one..!!'),404   
                  
        except KeyError as e:
            # Handle missing fields in the JSON data
            response = jsonify("Some field is missing! Please check the field and retry")
            response.status_code = 400  # Bad Request
            logger.error(f"KeyError: {e}")
            return response
            
        except pymysql.Error as db_error:
            # Handle database errors
            response = jsonify(f"Database Error: {db_error}")
            response.status_code = 500  # Internal Server Error
            logger.error(f"Database Error: {e}")
            return response
        except Exception as e:
            response = jsonify("An error occurred while processing your request: {e}")
            response.status_code = 500  # Internal Server Error
            logger.error(f"Internal Error: {e}")
            return response
           

