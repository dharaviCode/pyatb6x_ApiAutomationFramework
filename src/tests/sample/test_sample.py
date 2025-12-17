import pytest
import allure
import requests

@allure.title("Verify if test framework is working")
@pytest.mark.smoke
def test_sample_pass():
    assert True == True

@allure.title("Verify if test framework is not working")
@pytest.mark.regression
def test_sample_fail():
    assert False == True

