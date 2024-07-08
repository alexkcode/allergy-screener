import pytest
import dags.scraper

def test_scrape():
    return_value = dags.scraper.scrape_yelp_reviews()
    print(return_value)
    assert return_value is not None
