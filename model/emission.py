from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

from configs.config import db

class Country(db.Model):
    __tablename__ = 'country'
    
    country_id = Column(Integer, primary_key=True)
    country_name = Column(String(50), nullable=False)
    
    # Define a one-to-many relationship to EF_Factors
    emission_factors = relationship('EF_Factors', back_populates='country')
    # Define a one-to-many relationship to State
    states = relationship('State', back_populates='country')
   

class State(db.Model):
    __tablename__ = 'state'
    
    state_id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey('country.country_id'), nullable=False)
    state_name = Column(String(50), nullable=False)
    
    # Define a one-to-many relationship to EF_Factors
    emission_factors = relationship('EF_Factors', back_populates='state')
    # Define a many-to-one relationship to Country
    country = relationship('Country', back_populates='states')


# class Facility(db.Model):
#     __tablename__ = 'facility'
    
#     facility_id = Column(Integer, primary_key=True)
#     country_id = Column(Integer, ForeignKey('country.country_id'), nullable=False)
#     state_id = Column(Integer, ForeignKey('state.state_id'), nullable=False)
#     facility = Column(String(50), nullable=False)
    
#     # Define a one-to-many relationship to EF_Factors
#     emission_factors = relationship('EF_Factors', back_populates='facility')
#     # Define a many-to-one relationship to Country
#     country = relationship('Country', back_populates='facilities')
#     state = relationship('State', back_populates='facilities')


class Fuel(db.Model):
    __tablename__ = 'fuel'
    
    fuel_id = Column(Integer, primary_key=True)
    fuel_name = Column(String(50), nullable=False)
    
    # Define a one-to-many relationship to EF_Factors
    emission_factors = relationship('EF_Factors', back_populates='fuel')
    


class EF_Factors(db.Model):
    __tablename__ = 'emission_factors'
    
    emission_factor_id = Column(Integer, primary_key=True)
    emission_source = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    country_id = Column(Integer, ForeignKey('country.country_id'), nullable=False)
    state_id = Column(Integer, ForeignKey('state.state_id'), nullable=False)
    fuel_id = Column(Integer, ForeignKey('fuel.fuel_id'), nullable=False)
    value = Column(Float, nullable=False)
    unit = Column(String(50), nullable=False)
    remarks = Column(String(250), nullable=False)
    
    # Define relationships to Country, State, and Facility
    country = relationship('Country', back_populates='emission_factors')
    state = relationship('State', back_populates='emission_factors')
    fuel = relationship('Fuel', back_populates='emission_factors')
    
class GWP_Values(db.Model):
    __tablename__ = 'ghg_gwp'
    
    gwp_id = Column(Integer, primary_key=True)
    GHG= Column(String(50), nullable=False)
    source_name = Column(String(50), nullable=False)
    value = Column(Float, nullable=False)
    unit = Column(String(50), nullable=False)
    source = Column(String(50), nullable=False)

    
class User(db.Model):
    __tablename__ = 'user'
    
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    