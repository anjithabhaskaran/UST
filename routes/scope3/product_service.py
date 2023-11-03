from services.logger import logger
from flask import jsonify, request
from flask_restx import Api, Resource, fields, Namespace
from model.emission import *
from configs.config import db
import pymysql
from routes.jwt import tocken_required

# Configure the Flask-RESTx API
# Create a namespace for ProductService operations
product_service_name_space = Namespace('scope3/products_services_spend', description='ProductService related operations')
# Define the data model for ProductService Emission
prod_service_emission_model = product_service_name_space.model('ProductServiceEmissionModel', {
    'Year': fields.Integer(required=True),
    'Country': fields.String(required=True),
    'Service Type': fields.String(required=True),
    'Spend in Dollar': fields.Float(required=True),
    'Quantity': fields.Float(required=True)
   
})
# Create an endpoint for handling ProductService Emission
@product_service_name_space.route('')
class Scope3_prod_serives_API(Resource):
    @product_service_name_space.expect(prod_service_emission_model)
    @product_service_name_space.doc(security='Bearer')
    @tocken_required
    def post(self):
        try:
            json_data = request.json
            year = json_data['Year']
            country = json_data['Country']
            service_type= json_data['Service Type']
            cost = json_data['Spend in Dollar']
            quantity = json_data['Quantity']
            
            # Query the database using SQLAlchemy
            # TOTAL EMISSION = SPEND IN DOLLAR * QUANTITY * EMISSION PER UNIT
            emission_per_unit= (
                db.session.query(EF_Factors.value)
                .join(Country, EF_Factors.country_id == Country.country_id)
                .filter(EF_Factors.emission_source ==service_type ,Country.country_name == country, EF_Factors.year == year)
                .first()
            )
            
            if emission_per_unit:
                emission_per_unit_value = emission_per_unit[0]
                cost = float(cost)
                emission_per_unit_value = float(emission_per_unit_value)
                total_emission =( cost * quantity * emission_per_unit_value)/1000
                         
                
                response_data = {
                    "Total_emission": total_emission,
                    "emission_per_unit": emission_per_unit_value
                }
                response = jsonify(response_data)
                response.status_code = 200
                return response
            else:
                # Handle the case when emission_per_unit is not found
                response = jsonify("Could not find emission_per_unit for the particular region in this year")
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

