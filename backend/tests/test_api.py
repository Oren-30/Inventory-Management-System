import json

def test_get_inventory(client):
    response = client.get("/inventory")
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_single_item(client):
    response = client.get("/inventory/1")
    assert response.status_code in [200, 404]


def test_post_inventory(client):
    payload = {
        "barcode": "3017620422003",
        "quantity": 5,
        "price": 500
    }

    response = client.post(
        "/inventory",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code in [201, 404]


def test_patch_inventory(client):
    payload = {"price": 999}

    response = client.patch(
        "/inventory/1",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code in [200, 404]


def test_delete_inventory(client):
    response = client.delete("/inventory/1")
    assert response.status_code in [200, 404]