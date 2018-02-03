import pytest
@pytest.fixture(scope='function')
def test_name(request):
    return request.function.__name__
