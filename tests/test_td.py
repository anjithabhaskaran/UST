import pytest
from routes.scope3.t_d_loss import td_name_space  # Replace 'your_module' with the actual module where the API is defined
from configs.config import app  # Replace 'your_app' with the Flask app instance

@pytest.fixture
def client():
    # Create a test client using your Flask app
    with app.test_client() as client:
        yield client

def test_successful_post_request(client):
    # Prepare a valid request payload
    valid_payload = {
        'Year': 2023,
        'Country': 'United States',
        'State': 'California',
        'Loss': 1000.0
    }

    response = client.post('/scope3/energy_t&d_loss', json=valid_payload)

    assert response.status_code == 200
    data = response.get_json()
    assert "Total_emission" in data
    assert "emission_factor" in data

def test_missing_field_request(client):
    # Prepare a request with a missing field
    invalid_payload = {
        'Year': 2023,
        'Country': 'United States',
        'State': 'California',
    }

    response = client.post('/scope3/energy_t&d_loss', json=invalid_payload)

    assert response.status_code == 400

def test_emission_factor_not_found(client):
    # Prepare a request with a combination for which the emission factor is not found
    payload = {
        'Year': 2023,
        'Country': 'NonExistentCountry',
        'State': 'NonExistentState',
        'Loss': 1000.0
    }

    response = client.post('/scope3/energy_t&d_loss', json=payload)

    assert response.status_code == 404
    data = response.get_data(as_text=True)
    assert "Could not find emission factor for the particular region in this year" in data

# Add more test cases to cover other scenarios

if __name__ == "__main__":
    pytest.main()
