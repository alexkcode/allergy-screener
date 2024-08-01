import requests
import responses
import json
import os
import config.yelp as yelp


def get_business_search_response(response_file):
    # from Yelp's API reference examples
    # https://docs.developer.yelp.com/reference/v3_business_search
    url = "https://api.yelp.com/v3/businesses/search?sort_by=best_match&limit=20"

    headers = {'accept': 'application/json',
               'Authorization': yelp.get_api_key()}

    response = requests.get(url, headers=headers)

    with open(response_file, 'w') as json_file:
        json.dump(response, json_file, indent=4) 
    

def mock_business_search_yelp_response():
    response_file = 'yelp_business_search_response.json'
    if not os.path.exists(response_file):
        get_business_search_response(response_file)
    response_json = json.load(open(response_file))
    resp = responses.Response(
        method='GET',
        url='',
        json=response_json
    )
    responses.RequestsMock().add(resp)
    pass