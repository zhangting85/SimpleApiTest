import pytest
from core.data_reader import JsonTemplateReader


@pytest.fixture(scope="function")
def json_template(request):
    """
    this fixture is to use the json template reader to read the template and render it.
    the kwargs
    :param request: it is the pytest fixture request, contains the test name we need.
    :return: return the inner function which actually do the task.
    """
    def _to_read_the_template_by_test_name(**kwargs):
        return JsonTemplateReader().get_data(request.function.__name__, **kwargs)
    return _to_read_the_template_by_test_name
