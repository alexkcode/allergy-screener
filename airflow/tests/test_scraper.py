import pytest
import yelp_mock
import dags.scraper

@pytest.fixture(autouse=True)
def yelp_business_search_mock():
    yelp_mock.mock_business_search_yelp_response()

def test_scraper_has_valid_output():
    return_value = dags.scraper.scrape_yelp_reviews()
    print(return_value)
    assert return_value is not None
    assert False
