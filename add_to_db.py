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
# insert_query = """INSERT INTO country (country_id, country_name) VALUES (4, 'USA')"""
#insert_query = """INSERT INTO country ( country_name) VALUES ( 'Germany')"""
# insert_query = """INSERT INTO country (country_name) VALUES ( 'Israel')"""
# insert_query = """INSERT INTO country ( country_name) VALUES ( 'Malaysia')"""
# insert_query = """INSERT INTO country ( country_name) VALUES ( 'Mexico')"""
# insert_query = """INSERT INTO country ( country_name) VALUES ( 'Philipines')"""
# insert_query = """INSERT INTO country ( country_name) VALUES ( 'Poland')"""
# insert_query = """INSERT INTO country ( country_name) VALUES ( 'Singapore')"""
# insert_query = """INSERT INTO country ( country_name) VALUES ( 'Spain')"""
# insert_query = """INSERT INTO country ( country_name) VALUES ( 'UK')"""
# insert_query = """INSERT INTO country ( country_name) VALUES ( 'Bulgaria')"""
# insert_query = """INSERT INTO country ( country_name) VALUES ( 'Canada')"""

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
# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('electricity',2023,1,NULL,NULL,0.79, 'tCO2e/MWh','NULL')"""
# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('electricity',2023,2,NULL,NULL,0.052, 'tCO2e/MWh','NULL')"""
# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id,value, unit, remarks) VALUES ('electricity',2023,3,NULL,NULL,0.66375, 'tCO2e/MWh','NULL')"""

# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('electricity',2023,4,NULL,NULL,0.3712, 'tCO2e/MWh','NULL')"""
# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('electricity',2023,5,NULL,NULL,0.338, 'tCO2e/MWh','NULL')"""
# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('electricity',2023,6,NULL,NULL,0.696, 'tCO2e/MWh','NULL')"""
# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('electricity',2023,7,NULL,NULL,0.5322, 'tCO2e/MWh','NULL')"""
# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('electricity',2023,8,NULL,NULL,0.352, 'tCO2e/MWh','NULL')"""
# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('electricity',2023,9,NULL,NULL,0.7122, 'tCO2e/MWh','NULL')"""
# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('electricity',2023,10,NULL,NULL,0.789, 'tCO2e/MWh','NULL')"""
# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('electricity',2023,11,NULL,NULL,0.408, 'tCO2e/MWh','NULL')"""
# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('electricity',2023,12,NULL,NULL,0.1900, 'tCO2e/MWh','NULL')"""
# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('electricity',2023,13,NULL,NULL,0.1934, 'tCO2e/MWh','NULL')"""
# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('electricity',2023,14,NULL,NULL,0.4210, 'tCO2e/MWh','NULL')"""
# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('electricity',2023,15,NULL,NULL,0.1300, 'tCO2e/MWh','NULL')"""








# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('mobile/stationary',2023,1,NULL,1,0.00275, 'tCO2e/L','source:IPCC, formula:ef_factor from IPCC*density')"""
# insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('e-waste',2023,1,2,NULL, 5.0, 'tCO2e/ton','s3 Assumption, avg of emission is taken')"""
insert_query = """INSERT INTO emission_factors (emission_source,year,country_id, state_id,fuel_id, value, unit, remarks) VALUES ('computers&laptops',2023,1,NULL,NULL,0.0238, 'kgCO2e/USD','NULL')"""

# # #insert into goods and services
# # insert_query = """INSERT INTO  goods_and_services(created_on,modified_on,servive_type, consumption_end_date,consumption_start_date,cost,cost_unit,data_quality_type,descriiption,country_id,state_id,facility_id,quantity,quantity_unit, vender_id) VALUES (NULL,NULL,'Laptop',NULL,NULL,1093.96,'$','NULL','NULL',1,2,1,2400, 'kg',NULL)"""

# # insert into GHE_GWP
#insert_query = """INSERT INTO ghg_gwp(gwp_id, GHG,source_name,value, unit, source) VALUES (1,'HFC','R410a',2088,'CO2e','NULL')"""
#insert_query = """INSERT INTO ghg_gwp(gwp_id, GHG,source_name,value, unit, source) VALUES (2,'HCFC','R22',1810,'CO2e','NULL')"""




# user_name = 'admin'
# password = 'Abc@1234'
# # # Hash the password using bcrypt
# hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# # print(hashed_password)
# insert_query = """INSERT INTO user (user_name,password) VALUES (%s, %s)"""
# bind_data = ( user_name,hashed_password)
# # Execute the insert query
# cursor.execute(insert_query,bind_data)

cursor.execute(insert_query)
# Commit the transaction
commitConnection()

# Close the cursor and database connection
cursor.close()
closeConnection()
print("data added succesfully")
