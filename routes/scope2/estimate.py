from services.logger import logger
from flask import jsonify, request
from flask_restx import Api, Resource, fields , Namespace
from model.emission import *
from configs.config import db
import pymysql
from routes.jwt import tocken_required

# Configure the Flask-RESTx API
# Create a namespace for Scope two related operations
scope2_name_space = Namespace('scope2', description='Scope two related operations')
# Define the data model for ScopeTwoEmissionModel
scope2_emission_model = scope2_name_space.model('ScopeTwoEmissionModel', {
    'Year': fields.Integer(required=True),
    'Country': fields.String(required=True),
    'State': fields.String(required=True),
    'Total_Grid_Consumption': fields.Float(required=True)
})

# Create an endpoint for handling Scope Two Emission
@scope2_name_space.route('/estimate')
class Scope2API(Resource):
    @scope2_name_space.expect(scope2_emission_model)
    @scope2_name_space.doc(security='Bearer')
    @tocken_required
    def post(self):
        try:
            json_data = request.json
            year = json_data['Year']
            country = json_data['Country']
            # state = json_data['State']
            consumption = json_data['Total_Grid_Consumption']

            #uses grid average emission factors data: e-Grid subregion emission factors, 
            # which divide the U.S. into different regions approximating grid distribution. 
            # This is based on the electrical grid and not off of arbitrary state and city boundaries
            
            # Query the database using SQLAlchemy
            # TOTAL EMISSION = CONSUMPTION * ELECTRICITY EMISSION FACTOR
            emission_factor = (
                db.session.query(EF_Factors.value)
                .join(Country, EF_Factors.country_id == Country.country_id)
                .filter(EF_Factors.emission_source == 'electricity',Country.country_name == country, EF_Factors.year == year)
                .first()
            )
            
            if emission_factor:
                emission_factor_value = emission_factor[0]
                print(emission_factor_value)
                consumption = float(consumption)
                emission_factor_value = float(emission_factor_value)
                total_emission = consumption * emission_factor_value
                
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

