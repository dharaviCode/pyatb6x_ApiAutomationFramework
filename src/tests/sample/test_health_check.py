import pytest
import requests
import faker
import jsonschema



def test_google_health():
    response = requests.get("https://httpbin.org/get")
    print("Health check response")
    assert response.status_code == 200