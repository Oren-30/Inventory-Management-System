from unittest.mock import patch
import cli


@patch("builtins.input", side_effect=["3017620422003"])
@patch("cli.requests.get")
def test_search_product(mock_get, mock_input):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "product_name": "Nutella",
        "brand": "Ferrero",
        "ingredients": "Sugar",
        "categories": "Spread",
        "nutrition_grade": "E",
        "image": "url"
    }

    cli.search_product()
    assert True  # ensures function runs without crashing