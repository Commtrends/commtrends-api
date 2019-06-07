import os
from json import load
from random import randint


def get_random_campaign():
    current_path = os.path.abspath(os.path.dirname(__file__))
    file_name = "../resources/CampaignDetailsDashboard{_id}.json".format(_id=randint(1, 3))
    path = os.path.join(current_path, file_name)
    with open(path) as f:
        return load(f)
