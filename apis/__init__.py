from flask_restx import Api
# Import the namespaces (API routes) from different modules
from routes.scope1.fugitive_gas import fugitive_name_space as ns1
from routes.scope1.mobile_fuel import mobile_name_space as ns2
from routes.scope1.stationary_fuel import stationary_name_space as ns3
from routes.scope2.estimate import scope2_name_space as ns4
from routes.scope3.e_waste import ewaste_name_space as ns5
from routes.scope3.employee_commute import employee_commute_name_space as ns6
from routes.scope3.product_service import product_service_name_space as ns7
from routes.scope3.t_d_loss import td_name_space as ns8
from routes.auth import login_name_space as ns9



# Create an instance of the Flask-RESTx API
# Authorization = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}
authorizations={
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
}
# Authorization = {
#     'api_key' : {
#         'type' : 'apiKey',
#         'in' : 'header',
#         'name' : 'Authorization'
#     }
# }



api = Api(
    title='Sustainability',
    version='1.0',
    description='A description',
    authorizations=authorizations

    # All API metadatas
)
# Add each namespace (API route) to the API
api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)
api.add_namespace(ns4)
api.add_namespace(ns5)
api.add_namespace(ns6)
api.add_namespace(ns7)
api.add_namespace(ns8)
api.add_namespace(ns9)