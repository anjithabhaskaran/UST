from services.logger import logger
from flask import jsonify, request
from flask_restx import Api, Resource, fields, Namespace
from model.emission import GWP_Values
from configs.config import db
import pymysql
from routes.jwt import tocken_required


# Configure the Flask-RESTx API
# Create a namespace for Fugitive gas related operations
fugitive_name_space = Namespace('scope1/chemical_refrigerent_emission', description='Fugitive gas related operations')

# Define the data model for Fugitive Emissions
fugitive_emission_model = fugitive_name_space.model('FugitiveEmissionModel', {
    'GHG':fields.String(required=True),
    'Source_name':fields.String(required=True),
    'Leakage': fields.Float(required=True)
})

# Create an endpoint for handling Fugitive Emissions
@fugitive_name_space.route('')

class Scope1_fugitive_API(Resource):
    @fugitive_name_space.expect(fugitive_emission_model)
    @fugitive_name_space.doc(security='Bearer')
    @tocken_required
    def post(self):
        try:
            json_data = request.json
            GHG = json_data['GHG']
            source_name = json_data['Source_name']
            leakage = json_data['Leakage']
            
            # Query the database using SQLAlchemy to get GWP (Global Warming Potential) value
            # TOTAL EMISSION = LEAKAGE * GWP VALUE
            gwp_value = (
                db.session.query(GWP_Values.value)
                .filter(GWP_Values.GHG == GHG,GWP_Values.source_name == source_name)
                .first()
            )
            
            if gwp_value:
                gwp_value = gwp_value[0]
                leakage = float(leakage)
                gwp_value = float(gwp_value)
                total_emission = leakage * gwp_value
                
                response_data = {
                    "Total_emission": total_emission,
                    "gwp_value": gwp_value
                }
                response = jsonify(response_data)
                response.status_code = 200
                return response
            else:
                # Handle the case when GWP value is not found
                response = jsonify("Could not find gwp_value for the particular substance")
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

