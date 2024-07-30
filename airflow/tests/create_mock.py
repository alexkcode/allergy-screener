import requests
import responses
import json

def get_yelp_business_search_response():
    # from Yelp's API reference examples
    # https://docs.developer.yelp.com/reference/v3_business_search
    url = "https://api.yelp.com/v3/businesses/search?sort_by=best_match&limit=20"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    with open('yelp_business_search_response.json', 'w') as json_file:
        json.dump(response, json_file, indent=4) 
    

def mock_basic_yelp_response():
    resp = responses.Response(
        method='GET',
        url='',
        json={}
    )
    responses.add(resp)
    pass