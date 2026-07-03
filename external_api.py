import requests
from inventory import get_product_by_barcode

BASE_URL = "https://world.openfoodfacts.org/api/v2/product"


def fetch_product_by_barcode(barcode):
    """
    Fetch product details using a barcode.

    Returns:
        dict: Product information
        None: If product is not found
    """

    url = f"{BASE_URL}/{barcode}.json"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        if data.get("status") == 1:

            product = data.get("product", {})

            return {
                "barcode": barcode,
                "product_name": product.get("product_name", "Unknown Product"),
                "brand": product.get("brands", "Unknown Brand"),
                "ingredients": product.get("ingredients_text", ""),
                "categories": product.get("categories", ""),
                "nutrition_grade": product.get("nutriscore_grade", "N/A"),
                "image": product.get("image_front_url", "")
            }