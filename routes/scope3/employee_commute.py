from services.logger import logger
from flask import jsonify, request
from flask_restx import Api, Resource, fields, Namespace
from model.emission import *
from configs.config import db
import pymysql
from routes.jwt import tocken_required

# Configure the Flask-RESTx API
# Create a namespace for Employee Commute operations
employee_commute_name_space = Namespace('scope3/employee_commute', description='EmployeeCommute related operations')
# Define the data model for Employee Commute Emission
employee_emission_model = employee_commute_name_space.model('EmployeeCommuteEmissionModel', {
    'Year': fields.Integer(required=True),
    'Country': fields.String(required=True),
    'Number_of_employees': fields.Integer(required=True),
    'Average_commute_distance': fields.Float(required=True),
    'Average_commute_days': fields.Integer(required=True),
    'Fuel_type': fields.String(required=True)
})
# Create an endpoint for handling Employee Commute Emission
@employee_commute_name_space.route('')
class Scope3_employee_commute_API(Resource):
    @employee_commute_name_space.expect(employee_emission_model)
    @employee_commute_name_space.doc(security='Bearer')
    @tocken_required
    def post(self):
        try:
            json_data = request.json
            year = json_data['Year']
            country = json_data['Country']
            number = json_data['Number_of_employees']
            distance = json_data['Average_commute_distance']
            frequency = json_data['Average_commute_days']
            fuel_type = json_data['Fuel_type']
            
            # Query the database using SQLAlchemy
            # TOTAL EMISSION = AVERAGE COMMUTE DISTANCE * AVERAGE COMMUTE DAYS * NUMBER OF EMPLOYEES * EMISSION FACTOR OF FUEL
            emission_factor = (
                db.session.query(EF_Factors.value)
                .join(Country, EF_Factors.country_id == Country.country_id)\
                .join(Fuel, EF_Factors.fuel_id == Fuel.fuel_id)
                .filter(EF_Factors.emission_source =='mobile/stationary',Country.country_name == country, EF_Factors.year == year, Fuel.fuel_name == fuel_type)
                .first()
            )
            if emission_factor:
                emission_factor_value = emission_factor[0]
                print(emission_factor_value)
                emission_factor_value = float(emission_factor_value)
                total_emission = distance * frequency *  number * emission_factor_value
                
                response_data = {
                    "Total_emission": total_emission,
                    "emission_factor": emission_factor_value
                }
                response = jsonify(response_data)
                response.status_code = 200
                return response
            else:
                # Handle the case when emission factor is not found
                response = jsonify("Could not find emission factor for the particular region in this year")
                response.status_code = 404  # Proper error code for not found
                return response

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
             # Handle other unexpected errors
            response = jsonify("An error occurred while processing your request.")
            response.status_code = 500  # Internal Server Error
            logger.error(f"Internal Error: {e}")
            print(e)
            return response

