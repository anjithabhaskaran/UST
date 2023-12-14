import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="carbonfootprint"
)


# MASTER TABLES
# COUNTRY
# db_Create_Main_Table_Querys = """
# CREATE TABLE country
# (
#     country_id INT AUTO_INCREMENT PRIMARY KEY,
#     country_name VARCHAR(50) NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
# )
#  """
 
# # STATE
# db_Create_Main_Table_Querys = """
# CREATE TABLE state
# (
#     state_id INT AUTO_INCREMENT PRIMARY KEY,
#     country_id INT(20) NOT NULL, 
#     state_name VARCHAR(50) NOT NULL,
#     FOREIGN KEY (country_id) REFERENCES country(country_id),
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
# )
# """

# # # create table for facility
# db_Create_Main_Table_Querys = """
# CREATE TABLE facility
# (
#     facility_id INT AUTO_INCREMENT PRIMARY KEY,
#     country_id INT(20) NOT NULL,
#     state_id INT(20) NOT NULL,  
#     facility VARCHAR(50) NOT NULL,
#     FOREIGN KEY (country_id) REFERENCES country(country_id),
#     FOREIGN KEY (state_id) REFERENCES state(state_id),

# )
# """
# #OTHER REQUIRED TABLES

# # EMISSION FACTOR
db_Create_Main_Table_Querys = """CREATE TABLE emission_factors
(
    emission_factor_id INT AUTO_INCREMENT PRIMARY KEY,
    emission_source varchar(250) not null,
    year int(100) not null,
    country_id int(100) not null,
    state_id int(100),
    fuel_id int(100),
    value float not null, 
    unit varchar(50) not null,
    remarks varchar(50) not null,
    FOREIGN KEY (country_id) REFERENCES country(country_id),
    FOREIGN KEY (state_id) REFERENCES state(state_id),
    FOREIGN KEY (fuel_id) REFERENCES fuel(fuel_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
)"""

# # E- GRID SUB REGIONS - for scope 2
# db_Create_Main_Table_Querys = """
# CREATE TABLE e_grid_sub_regions
# (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     country_id INT(20) NOT NULL, 
#     e_grid_sub_regions VARCHAR(50) NOT NULL,
#     ef_factor float not null, 
#     unit varchar(50) not null,
#     FOREIGN KEY (country_id) REFERENCES country(country_id)
# )
# # # """

# #create table for gwp_values
# db_Create_Main_Table_Querys = """CREATE TABLE ghg_gwp
# (
#     gwp_id INT AUTO_INCREMENT PRIMARY KEY,
#     GHG varchar(100) not null,
#     source_name varchar(100) not null,
#     value float not null, 
#     unit varchar(50) not null,
#     source varchar(200) not null,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
# )"""


# create table for fuel details
# db_Create_Main_Table_Querys = """CREATE TABLE fuel
# (
#     fuel_id INT AUTO_INCREMENT PRIMARY KEY,
#     fuel_name varchar(100) not null,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP); 
# )"""


# #create table for user details
# db_Create_Main_Table_Querys = """CREATE TABLE user
# (
#     user_id INT AUTO_INCREMENT PRIMARY KEY,
#     user_name varchar(100) not null,
#     password varchar(250) not null,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP); 
# )"""

# Execute queries
cursor = mydb.cursor()
# # Create Main_table table
cursor.execute(db_Create_Main_Table_Querys)
print("Main_table table created successfully")

cursor.close()
mydb.close()
