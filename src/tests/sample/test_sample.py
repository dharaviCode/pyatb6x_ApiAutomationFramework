import pytest
import allure
import requests

@allure.title("Verify if test framework is working")
@pytest.mark.smoke
@allure.step("Step 1")
def test_sample_pass():
    assert True == True

@allure.title("Verify if test framework is not working")
@pytest.mark.regression
@allure.step("Step 2")
def test_sample_fail():
    assert False == True

