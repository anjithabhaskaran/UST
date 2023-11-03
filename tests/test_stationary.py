import pytest
from routes.scope1.stationary_fuel import stationary_name_space  
from configs.config import app  
@pytest.fixture
def client():
    # Create a test client using your Flask app
    with app.test_client() as client:
        yield client

def test_successful_post_request(client):
    # Prepare a valid request payload
    valid_payload = {
        'Year': 2023,
        'Country': 'India',
        'Fuel_type': 'Diesel',
        'Fuel_Consumption': 1000.0
    }

    response = client.post('/scope1/fuel_combustion_emission_static', json=valid_payload)

    assert response.status_code == 200
    data = response.get_json()
    assert "Total_emission" in data
    assert "emission_factor" in data

def test_missing_field_request(client):
    # Prepare a request with a missing field
    invalid_payload = {
        'Year': 2023,
        'Country': 'India',
        'Fuel_type': 'Diesel',
    }

    response = client.post('/scope1/fuel_combustion_emission_static', json=invalid_payload)

    assert response.status_code == 400

def test_emission_factor_not_found(client):
    # Prepare a request with a combination for which emission factor is not found
    payload = {
        'Year': 2023,
        'Country': 'NonExistentCountry',
        'Fuel_type': 'NonExistentFuelType',
        'Fuel_Consumption': 1000.0
    }

    response = client.post('/scope1/fuel_combustion_emission_static', json=payload)

    assert response.status_code == 404
    data = response.get_data(as_text=True)
    assert "Could not find emission factor for the particular region in this year" in data

# Add more test cases to cover other scenarios

if __name__ == "__main__":
    pytest.main()
