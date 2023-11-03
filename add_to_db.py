import mysql.connector
from services.db_service import *
from app import app
import bcrypt
# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="carbonfootprint"
)

# #SQL query to insert values

# # #insert into table - country
#insert_query = """INSERT INTO country (country_id, country_name) VALUES (1, 'India')"""
#insert_query = """INSERT INTO country (country_id, country_name) VALUES (2, 'France')"""
#insert_query = """INSERT INTO country (country_id, country_name) VALUES (3, 'Australia')"""
#insert_query = """INSERT INTO country (country_id, country_name) VALUES (4, 'US')"""

# # #insert into table - state
#insert_query = """INSERT INTO state ( country_id, state_name) VALUES ( 1,'Karnataka')"""
#insert_query = """INSERT INTO state ( country_id, state_name) VALUES ( 1,'Kerala')"""
#insert_query = """INSERT INTO state ( country_id, state_name) VALUES ( 3,'Victoria')"""
#insert_query = """INSERT INTO state ( country_id, state_name) VALUES ( 3,'New South Wales')"""

# # #insert into table - facility
#insert_query = """INSERT INTO facility ( country_id, state_id,facility) VALUES ( 1,2,'Brigade-kochi')"""
#insert_query = """INSERT INTO facility ( country_id, state_id,facility) VALUES ( 1,2,'Vismaya-Kochi')"""
#insert_query = """INSERT INTO facility ( country_id, state_id,facility) VALUES ( 3,4,'Sydney')"""



# # # # #insert into table - egrid sub regions
#insert_query = """INSERT INTO e_grid_sub_regions ( country_id, e_grid_sub_regions, ef_factor, unit) VALUES ( 4,'NEWE (NPCC New England)',528.2,'lb / MWh')"""

# #insert into fuel table
#insert_query = """INSERT INTO fuel ( fuel_name) VALUES ( 'Diesel')"""
#insert_query = """INSERT INTO fuel ( fuel_name) VALUES ( 'Petrol')"""


# # # insert into table - emission_factors
# insert_query = """INSERT INTO emission_factors (id,emission_source,year,country_id, state_id,facility_id,fuel_id, value, unit, remarks) VALUES (1,'electricity',2023,1,2,NULL,NULL,0.79, 'tCO2e/MWh','NULL')"""
# insert_query = """INSERT INTO emission_factors (id,emission_source,year,country_id, state_id,facility_id,fuel_id,value, unit, remarks) VALUES (2,'electricity',2023,3,3,NULL,NULL,0.66375, 'tCO2e/MWh','NULL')"""
#insert_query = """INSERT INTO emission_factors (id,emission_source,year,country_id, state_id,facility_id,fuel_id, value, unit, remarks) VALUES (3,'mobile/stationary',2023,1,NULL,NULL,1,0.00275, 'tCO2e/L','source:IPCC, formula:ef_factor from IPCC*density')"""
#insert_query = """INSERT INTO emission_factors (id,emission_source,year,country_id, state_id,facility_id,fuel_id, value, unit, remarks) VALUES (4,'e-waste',2023,1,2,1,NULL, 5.0, 'tCO2e/ton','s3 Assumption, avg of emission is taken')"""
# insert_query = """INSERT INTO emission_factors (id,emission_source,year,country_id, state_id,facility_id,fuel_id, value, unit, remarks) VALUES (5,'computers&laptops',2023,1,NULL,NULL,NULL,0.0238, 'kgCO2e/USD','NULL')"""

# # #insert into goods and services
# # insert_query = """INSERT INTO  goods_and_services(created_on,modified_on,servive_type, consumption_end_date,consumption_start_date,cost,cost_unit,data_quality_type,descriiption,country_id,state_id,facility_id,quantity,quantity_unit, vender_id) VALUES (NULL,NULL,'Laptop',NULL,NULL,1093.96,'$','NULL','NULL',1,2,1,2400, 'kg',NULL)"""

# # insert into GHE_GWP
# #insert_query = """INSERT INTO ghg_gwp(id, GHG,source_name,value, unit, source) VALUES (1,'HFC','R410a',2088,'CO2e','NULL')"""
# #insert_query = """INSERT INTO ghg_gwp(id, GHG,source_name,value, unit, source) VALUES (2,'HCFC','R22',1810,'CO2e','NULL')"""




user_name = 'anjitha'
password = 'Abc@1234'
# # Hash the password using bcrypt
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# print(hashed_password)
insert_query = """INSERT INTO user (user_name,password) VALUES (%s, %s)"""
bind_data = ( user_name,hashed_password)
# # Execute the insert query
cursor.execute(insert_query,bind_data)
#cursor.execute(insert_query)
# Commit the transaction
commitConnection()

# Close the cursor and database connection
cursor.close()
closeConnection()
print("data added succesfully")
