from flask import Flask, jsonify, request, render_template

from inventory import (
    get_all_items,
    get_item,
    add_item,
    update_item,
    delete_item
)
from external_api import fetch_product_by_barcode

app = Flask(__name__)



# Home Page

@app.route("/")
def home():
    return render_template("index.html")



# GET /inventory
# Fetch all inventory
@app.route("/inventory", methods=["GET"])
def inventory_list():
    return jsonify(get_all_items()), 200



# GET /inventory/<id>
# Fetch one inventory item

@app.route("/inventory/<int:item_id>", methods=["GET"])
def inventory_item(item_id):

    item = get_item(item_id)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item), 200



# POST /inventory
# Add inventory item

@app.route("/inventory", methods=["POST"])
def create_inventory():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON received"}), 400

    barcode = data.get("barcode")

    quantity = data.get("quantity")
    price = data.get("price")

    if not barcode:
        return jsonify({"error": "Barcode is required"}), 400

    # Fetch product details from OpenFoodFacts
    product = fetch_product_by_barcode(barcode)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    new_item = {
        "barcode": barcode,
        "product_name": product["product_name"],
        "brand": product["brand"],
        "quantity": quantity,
        "price": price
    }

    item = add_item(new_item)

    return jsonify(item), 201



# PATCH /inventory/<id>
# Update inventory

@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def edit_inventory(item_id):

    data = request.get_json()

    item = update_item(item_id, data)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item), 200



# DELETE /inventory/<id>

@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def remove_inventory(item_id):

    deleted = delete_item(item_id)

    if not deleted:
        return jsonify({"error": "Item not found"}), 404

    return jsonify({"message": "Item deleted successfully"}), 200


# -----------------------------
# GET Product From OpenFoodFacts
# -----------------------------
@app.route("/product/<barcode>", methods=["GET"])
def product_lookup(barcode):

    product = fetch_product_by_barcode(barcode)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product), 200



# Run Flask

if __name__ == "__main__":
    app.run(debug=True)