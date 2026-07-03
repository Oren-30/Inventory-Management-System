import requests

BASE_URL = "https://world.openfoodfacts.org/api/v2/product"

def fetch_product_by_barcode(barcode):
    url = f"{BASE_URL}/{barcode}.json"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        if data.get("status") != 1:
            return None

        product = data.get("product", {})

        return {
            "barcode": barcode,
            "product_name": product.get("product_name", ""),
            "brand": product.get("brands", ""),
            "ingredients": product.get("ingredients_text", ""),
            "categories": product.get("categories", ""),
            "nutrition_grade": product.get("nutriscore_grade", ""),
            "image": product.get("image_front_url", "")
        }

    except requests.exceptions.RequestException:
        return None


def fetch_product_by_name(name):
    url = "https://world.openfoodfacts.org/cgi/search.pl"

    params = {
        "search_terms": name,
        "search_simple": 1,
        "action": "process",
        "json": 1
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()

        data = response.json()

        if not data.get("products"):
            return None

        product = data["products"][0]

        return {
            "barcode": product.get("code", ""),
            "product_name": product.get("product_name", ""),
            "brand": product.get("brands", ""),
            "ingredients": product.get("ingredients_text", ""),
            "categories": product.get("categories", ""),
            "nutrition_grade": product.get("nutriscore_grade", ""),
            "image": product.get("image_front_url", "")
        }

    except requests.exceptions.RequestException:
        return None