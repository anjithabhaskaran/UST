from services.logger import logger
from flask import jsonify, request
from flask_restx import Api, Resource, fields, Namespace
from model.emission import *
from configs.config import app
import pymysql
from routes.jwt import tocken_required

# Configure the Flask-RESTx API
# Create a namespace for Stationary Fuel Emission operations
stationary_name_space = Namespace('scope1/fuel_combustion_emission_static', description='Stationary fuel related operations')
# Define the data model for Stationary Fuel Emission
stationary_emission_model = stationary_name_space.model('stationaryEmissionModel', {
    'Year': fields.Integer(required=True),
    'Country': fields.String(required=True),
    'Fuel_type':fields.String(required=True),
    'Fuel_Consumption': fields.Float(required=True)
})
# Create an endpoint for handling Stationary Fuel Emission
@stationary_name_space.route('')
class Scope1_stationary_API(Resource):
    @stationary_name_space.expect(stationary_emission_model)
    @stationary_name_space.doc(security='Bearer')
    @tocken_required
    def post(self):
        try:
            json_data = request.json
            year = json_data['Year']
            country = json_data['Country']
            fuel_type = json_data['Fuel_type']
            fuel_consumption = json_data['Fuel_Consumption']
            
             # Query the database using SQLAlchemy to get emission factor
             # TOTAL EMISSION = FUEL CONSUMPTION(L) * EMISSION FACTOR
            emission_factor = (
                db.session.query(EF_Factors.value)
                .join(Country, EF_Factors.country_id == Country.country_id)\
                .join(Fuel, EF_Factors.fuel_id == Fuel.fuel_id)
                .filter(EF_Factors.emission_source =='mobile/stationary',Country.country_name == country, EF_Factors.year == year, Fuel.fuel_name == fuel_type)
                .first()
            )
            
            if emission_factor:
                emission_factor_value = emission_factor[0]
                fuel_consumption = float(fuel_consumption)
                emission_factor_value = float(emission_factor_value)
                total_emission = fuel_consumption * emission_factor_value
                
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

