import pytest
import allure
import requests
from src.modules.wrapper.api_requests_wrapper import post_request
from src.endpoints.api_constants import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import payload_create_booking
from src.modules.verification.common_verification import *


@pytest.mark.positive
@allure.title("Verify successful create booking with 200 status code")
@allure.description("Create Booking with 200 status code")
@allure.severity(allure.severity_level.NORMAL)
def test_create_booking_positive():
     response = post_request(
         url = APIConstants().url_create_booking(),
         auth = None,
         headers = Utils().common_headers_json(),
         payload = payload_create_booking(),
         in_json = False
     )
     print(response)
     verify_status_code(response_data_status=response.status_code,expected_status_code=200)
     verify_json_key_for_not_null(response.json()["bookingid"])

     # auth ->  basic auth ( admin, password -> base64)
     # auth -> bearer auth ( api token) eydalkskldjasjdkja....

@pytest.mark.negative
@allure.title("Verify create booking error 500 status code with empty payload")
@allure.description("Booking not created with 500 status code for empty payload")
@allure.severity(allure.severity_level.MINOR)
def test_create_booking_negative_tc1():
         response = post_request(
             url=APIConstants().url_create_booking(),
             auth=None,
             headers=Utils().common_headers_json(),
             payload={},
             in_json=False
         )
         verify_status_code(response_data_status=response.status_code, expected_status_code=500)

@pytest.mark.negative
@allure.title("Verify create booking error 500 status code with incomplete payload")
@allure.description("Booking not created with 500 status code for incomplete payload")
@allure.severity(allure.severity_level.MINOR)
def test_create_booking_negative_tc2():
        response = post_request(
                 url=APIConstants().url_create_booking(),
                 auth=None,
                 headers=Utils().common_headers_json(),
                 payload={"first_name": "John"},
                 in_json=False
             )
        verify_status_code(response_data_status=response.status_code, expected_status_code=500)



