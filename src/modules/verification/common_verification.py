# This file will have all the common verification which is done on a fetched response.
# Verify the http status_code
# Verify the headers
# Verify the response data
# - Verify if the key value is not null or null
# - Verify the JSON Schema

def verify_status_code(response_data_status, expected_status_code):
    assert response_data_status == expected_status_code, "Failed to match the status code"

def verify_response_key(key, expected_data):
    assert key == expected_data, "Failed to match the response key"

def verify_json_key_for_not_null(key):
    assert key != 0, "Failed - Key is non Empty" + key
    assert key > 0, "Failed - Key is grater than zero"

def verify_json_key_for_not_null_token(key):
    assert key != 0, "Failed - Key is non Empty" + key

def verify_response_delete(response):
    assert "Created" in response
