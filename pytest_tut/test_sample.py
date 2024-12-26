import pytest

@pytest.fixture
def simple_fixture():
    return {"name":"narendra","age":25}


def test_simple_fixture(simple_fixture):
    assert simple_fixture["name"] == "narendra"
    assert simple_fixture["age"] == 25