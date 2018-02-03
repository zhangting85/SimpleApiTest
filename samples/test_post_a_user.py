import requests
from test_data_util.data_reader import read_json
import json
import pytest


testdata = [
    ("Tom", "TomX"),
    ("Colin", "ColinX"),
    ("Jim", "JimX"),
    ("King", "KingX"),
    ("AnyOne", "AnyOneX"),
]


@pytest.mark.parametrize("input_user,return_user", testdata)
def test_post_a_user(input_user, return_user,test_name):
    url = "http://localhost:8000/post_a_user"
    data = read_json(test_name, user=input_user)
    r = requests.post(url=url, data=data)
    assert r.status_code == 200
    assert json.loads(r.content)["your_input"] == return_user


if __name__ == "__main__":
    pytest.main()