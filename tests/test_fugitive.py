import pytest
from routes.scope1.fugitive_gas import fugitive_name_space  
from configs.config import app 

@pytest.fixture
def client():
    # Create a test client using your Flask app
    with app.test_client() as client:
        yield client

def test_successful_post_request(client):
    # Prepare a valid request payload
    valid_payload = {
        'GHG': 'HFC',
        'Source_name': 'R410a',
        'Leakage': 10.0
    }

    response = client.post('/scope1/chemical_refrigerent_emission', json=valid_payload)

    assert response.status_code == 200
    data = response.get_json()
    assert "Total_emission" in data
    assert "gwp_value" in data

def test_missing_field_request(client):
    # Prepare a request with a missing field
    invalid_payload = {
        'GHG': 'HCFC',
        'Leakage': 10.0
    }

    response = client.post('/scope1/chemical_refrigerent_emission', json=invalid_payload)

    assert response.status_code == 400

def test_gwp_value_not_found(client):
    # Prepare a request with GHG and Source_name for which GWP value is not found
    payload = {
        'GHG': 'NonExistentGHG',
        'Source_name': 'NonExistentSource',
        'Leakage': 10.0
    }

    response = client.post('/scope1/chemical_refrigerent_emission', json=payload)

    assert response.status_code == 404
    data = response.get_data(as_text=True)
    assert "Could not find gwp_value for the particular substance" in data

# Add more test cases to cover other scenarios

if __name__ == "__main__":
    pytest.main()
