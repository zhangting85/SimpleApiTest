import requests
import json
import pytest

testdata = [
    ("Tom", "TomX", 200),
    ("Colin", "ColinX", 200),
    ("Jim", "JimX", 200),
    ("King", "KingX", 200),
    ("AnyOne", "AnyOneX", 200),
]


@pytest.mark.parametrize("input_user,return_user,expected_response_code", testdata)
def test_post_a_user(input_user, return_user, expected_response_code, json_template):
    """
    this test is to do this:
    to post a http request to the server.
    the request body would be a json object.
    this json object is based on a template "test_post_a_user.json" and it actually look like this:{"user":"{{user}}"}
    then the test framework will change it to:
    {"user":"Tom"}
    {"user":"Colin"}
    {"user":"Jim"}
    {"user":"King"}
    {"user":"AnyOne"}
    Yes, you noticed, the only changing part of the test is the {{user}}, and the {{user}} would be rendered
    with the data you input here in the test case.

    and in the respective of testing, the true test data is also in 2 parts:
    the permanent part is in json template file.
    the changing part is in the case file.

    :param input_user: the changing user name in {{user}}
    :param return_user: the expected result of the server returns. here the server would return what you input + "X"
    :param expected_response_code: always 200, the server returns in this case.
    :param json_template: this is actually a fixture i defined in conftest.py and it will call the real template data
    reader to read the data.
    """
    url = "http://localhost:8000/post_a_user"
    data = json_template(user=input_user)
    r = requests.post(url=url, data=data)
    assert r.status_code == expected_response_code
    assert json.loads(r.content)["your_input"] == return_user


@pytest.mark.parametrize("input_user,return_user,expected_response_code", testdata)
def test_post_a_user2(input_user, return_user, expected_response_code, json_template):
    """
    to be shortly, it is just the same as in test_post_a_user. the only difference is:
    it use a different test name, so a different json file needed.
    :param input_user: the same
    :param return_user: the same
    :param expected_response_code: the same
    :param json_template: the same
    """
    url = "http://localhost:8000/post_a_user"
    data = json_template(user=input_user)
    r = requests.post(url=url, data=data)
    assert r.status_code == expected_response_code
    assert json.loads(r.content)["your_input"] == return_user



if __name__ == "__main__":
    pytest.main()
