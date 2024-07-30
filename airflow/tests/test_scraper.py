import pytest
import dags.scraper

def test_scraper_has_valid_output():
    return_value = dags.scraper.scrape_yelp_reviews()
    print(return_value)
    assert return_value is not None
    assert False
