import requests

BASE_URL = "http://127.0.0.1:5000"


def view_inventory():
    response = requests.get(f"{BASE_URL}/inventory")

    if response.status_code == 200:
        items = response.json()

        if not items:
            print("\nInventory is empty.\n")
            return

        print("\nInventory")
        print("-" * 60)

        for item in items:
            print(f"ID: {item['id']}")
            print(f"Name: {item['product_name']}")
            print(f"Brand: {item['brand']}")
            print(f"Barcode: {item['barcode']}")
            print(f"Quantity: {item['quantity']}")
            print(f"Price: {item['price']}")
            print("-" * 60)

    else:
        print("Error:", response.text)


def add_inventory():
    barcode = input("Barcode: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))

    payload = {
        "barcode": barcode,
        "quantity": quantity,
        "price": price
    }

    response = requests.post(
        f"{BASE_URL}/inventory",
        json=payload
    )

    if response.status_code == 201:
        print("\nItem added successfully.")
        print(response.json())
    else:
        print("Error:", response.text)


def update_inventory():
    item_id = input("Item ID: ")

    quantity = input("New quantity (leave blank to skip): ")
    price = input("New price (leave blank to skip): ")

    payload = {}

    if quantity:
        payload["quantity"] = int(quantity)

    if price:
        payload["price"] = float(price)

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=payload
    )

    if response.status_code == 200:
        print("\nItem updated.")
        print(response.json())
    else:
        print("Error:", response.text)


def delete_inventory():
    item_id = input("Item ID: ")

    response = requests.delete(
        f"{BASE_URL}/inventory/{item_id}"
    )

    if response.status_code == 200:
        print(response.json()["message"])
    else:
        print("Error:", response.text)


def search_product():
    barcode = input("Barcode: ")

    response = requests.get(
        f"{BASE_URL}/product/{barcode}"
    )

    if response.status_code == 200:
        product = response.json()

        print("\nProduct Details")
        print("-" * 40)
        print("Name:", product.get("product_name"))
        print("Brand:", product.get("brand"))
        print("Ingredients:", product.get("ingredients"))
        print("Categories:", product.get("categories"))
        print("Nutrition Grade:", product.get("nutrition_grade"))
        print("Image:", product.get("image"))

    else:
        print("Product not found.")


def menu():

    while True:

        print("\n===== Inventory Management =====")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Search Product (OpenFoodFacts)")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            add_inventory()

        elif choice == "3":
            update_inventory()

        elif choice == "4":
            delete_inventory()

        elif choice == "5":
            search_product()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()