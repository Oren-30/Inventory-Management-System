import requests

BASE_URL = "https://world.openfoodfacts.org/api/v2/product"

HEADERS = {
    "User-Agent": "InventoryManagementSystem/1.0 (Student Project)",
    "Accept": "application/json"
}

def fetch_product_by_barcode(barcode):
    url = f"{BASE_URL}/{barcode}.json"

    print("Request URL:", url)

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        print("Status Code:", response.status_code)

        # Check if the request was successful
        if response.status_code != 200:
            print("Server Response:")
            print(response.text)
            return None

        data = response.json()

        if data.get("status") != 1:
            print("Product not found.")
            return None

        product = data["product"]

        return {
            "barcode": barcode,
            "product_name": product.get("product_name", ""),
            "brand": product.get("brands", ""),
            "ingredients": product.get("ingredients_text", ""),
            "categories": product.get("categories", ""),
            "nutrition_grade": product.get("nutriscore_grade", ""),
            "image": product.get("image_front_url", "")
        }

    except requests.exceptions.RequestException as e:
        print("Network Error:", e)
        return None


if __name__ == "__main__":
    product = fetch_product_by_barcode("3017620422003")

    if product:
        print(product)
    else:
        print("No product returned.")