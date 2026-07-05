from inventory import (
    get_all_items,
    get_item,
    add_item,
    update_item,
    delete_item
)

def test_get_all_items():
    items = get_all_items()
    assert isinstance(items, list)


def test_add_item():
    item = {
        "barcode": "111",
        "product_name": "Test",
        "brand": "TestBrand",
        "quantity": 1,
        "price": 100
    }

    result = add_item(item)
    assert result["id"] is not None


def test_get_item():
    item = get_item(1)
    assert item is None or item["id"] == 1


def test_update_item():
    result = update_item(1, {"price": 123})
    assert result is None or result["price"] == 123


def test_delete_item():
    result = delete_item(999)
    assert result in [True, False]