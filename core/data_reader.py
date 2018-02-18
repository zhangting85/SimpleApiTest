from jinja2 import Environment, FileSystemLoader
import json


class JsonTemplateReader():
    def __init__(self):
        """
        it simply using jinja2 file system loader to load the json template file which should be in the same folder
        as the tests.
        """
        self.env = Environment(loader=FileSystemLoader('.'))

    def get_data(self, test_name, **kwargs):
        """
        to read the data from a json file which has the same name as the test name but end with .json. And this json
        file need to be in the same folder with the test cases.
        :param test_name: the test name
        :param kwargs: the data in the template is not complete, it is only a part or the permanent part of the json
        we would send in the request. and the changeable part will be transferred into by this kwargs.
        :return: it will return a json object created from the test_name.json and rendered with the data you
        transferred in kwargs.
        """
        template = self.env.get_template(test_name + ".json")
        return json.loads(template.render(**kwargs))
