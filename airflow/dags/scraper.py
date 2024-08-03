from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import requests

def scrape_yelp_reviews():
    # from Yelp's API reference examples
    # https://docs.developer.yelp.com/reference/v3_business_search
    url = "https://api.yelp.com/v3/businesses/search?sort_by=best_match&limit=20"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    
    return response.text
