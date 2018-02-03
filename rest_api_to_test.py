import hug
import json

@hug.get()
def hello():
    return "hello"


@hug.post()
def post_a_user(user):
    return {"your_input":user+"X"}

# use the following command to start the rest api which will be tested at your localhost:8000
# hug -f rest_api_to_test.py
