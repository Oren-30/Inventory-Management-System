# Mock OpenFoodFacts Products
# -----------------------------
mock_products = [
    {
        "id": 1,
        "barcode": "7613036243684",
        "status": 1,
        "product": {
            "product_name": "Organic Almond Milk",
            "brands": "Silk",
            "ingredients_text": "Filtered water, almonds, cane sugar",
            "categories": "Plant-Based Beverages",
            "nutriscore_grade": "A",
            "image_front_url": ""
        }
    },
    {
        "id": 2,
        "barcode": "5449000000996",
        "status": 1,
        "product": {
            "product_name": "Apple Juice",
            "brands": "Minute Maid",
            "ingredients_text": "Water, apple concentrate, vitamin C",
            "categories": "Fruit Juices",
            "nutriscore_grade": "B",
            "image_front_url": ""
        }
    },
    {
        "id": 3,
        "barcode": "3017620422003",
        "status": 1,
        "product": {
            "product_name": "Nutella",
            "brands": "Ferrero",
            "ingredients_text": "Sugar, palm oil, hazelnuts, cocoa",
            "categories": "Chocolate Spread",
            "nutriscore_grade": "E",
            "image_front_url": ""
        }
    }
]
# Inventory Database
# -----------------------------
inventory = [
    {
        "id": 1,
        "barcode": "7613036243684",
        "product_name": "Organic Almond Milk",
        "brand": "Silk",
        "quantity": 20,
        "price": 450
    },
    {
        "id": 2,
        "barcode": "5449000000996",
        "product_name": "Apple Juice",
        "brand": "Minute Maid",
        "quantity": 15,
        "price": 350
    }
]

next_inventory_id = 3


# -----------------------------
# Helper Functions
# -----------------------------
def get_all_items():
    """Return all inventory items."""
    return inventory


def get_item(item_id):
    """Return one inventory item by ID."""
    return next((item for item in inventory if item["id"] == item_id), None)


def add_item(item):
    """Add a new inventory item."""
    global next_inventory_id

    item["id"] = next_inventory_id
    next_inventory_id += 1

    inventory.append(item)

    return item


def update_item(item_id, updates):
    """Update an inventory item."""
    item = get_item(item_id)

    if not item:
        return None

    item.update(updates)

    return item


def delete_item(item_id):
    """Delete an inventory item."""
    item = get_item(item_id)

    if item:
        inventory.remove(item)
        return True

    return False


def get_product_by_barcode(barcode):
    """Search the mock OpenFoodFacts database."""
    for product in mock_products:
        if product["barcode"] == barcode:
            return product

    return None
