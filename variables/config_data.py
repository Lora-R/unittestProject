import os
import json

base_data = None


def load_base_data():
    global base_data
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'variables_for_tests.json')) as f:
        base_data = json.load(f)


load_base_data()
