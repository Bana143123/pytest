# Write a test that parametrizes values passed to a fixture.
# You are testing a system that generates user reports for a given user ID. 
# The fixture loads user data based on the user ID.

# Create a function generate_report(user_id) that generates a report for the given user ID. 
# The fixture user_data should simulate loading different user data based on the user ID.

import pytest

def generate_report(user_id):
    return f"Report for user {user_id}"

@pytest.fixture
def user_data(request):
    user_id = request.param
    return {"user_id": user_id,"data":f"Data for user {user_data}"}

@pytest.mark.parametrize("user_data",[1,2,3],indirect=True)
def test_generate_report(user_data):
    user_id = user_data["user_id"]
    expected_report = f"Report for user {user_id}"
    assert generate_report(user_id) == expected_report