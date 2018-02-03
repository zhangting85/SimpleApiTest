from jinja2 import Environment, FileSystemLoader
import json


class DataReader():
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader('.'))

    def get_data(self, test_name, **kwargs):
        template = self.env.get_template(test_name + ".json")
        return json.loads(template.render(**kwargs))


def read_json(test_name,**kwargs):
    return DataReader().get_data(test_name,**kwargs)