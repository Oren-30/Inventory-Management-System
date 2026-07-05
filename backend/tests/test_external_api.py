from unittest.mock import patch
from external_api import fetch_product_by_barcode


@patch("external_api.requests.get")
def test_fetch_product_success(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Test Product",
            "brands": "Test Brand"
        }
    }

    result = fetch_product_by_barcode("123")

    assert result is not None
    assert result["product_name"] == "Test Product"


@patch("external_api.requests.get")
def test_fetch_product_fail(mock_get):

    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = {}

    result = fetch_product_by_barcode("999")

    assert result is None