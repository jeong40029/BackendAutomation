import requests
from utilities.configurations import *
from utilities.resources import *


def after_scenario(context, scenario):
    if "library" in scenario.tags:
        deleteurl = getConfig()['API']['endpoint'] + Apiresources.deleteBook
        deletebook_response = requests.post(deleteurl, json={"ID": context.bookId}, headers=context.headers)

        assert deletebook_response.status_code == 200
        json_res = deletebook_response.json()
        print(json_res['msg'])

        assert json_res['msg'] == 'book is successfully deleted'