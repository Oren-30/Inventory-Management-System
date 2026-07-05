import { useState } from "react";
import api from "../api";

function EditProduct() {
  const [id, setId] = useState("");
  const [quantity, setQuantity] = useState("");
  const [price, setPrice] = useState("");

  const handleUpdate = async () => {
    if (!id) {
      alert("Please enter item ID");
      return;
    }

    const payload = {};

    if (quantity) payload.quantity = Number(quantity);
    if (price) payload.price = Number(price);

    try {
      await api.patch(`/inventory/${id}`, payload);
      alert("Item updated successfully!");
    } catch (err) {
      alert("Error updating item");
    }
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h3>Edit Product</h3>

      <input
        placeholder="Item ID"
        value={id}
        onChange={(e) => setId(e.target.value)}
      />

      <input
        placeholder="New Quantity"
        value={quantity}
        onChange={(e) => setQuantity(e.target.value)}
      />

      <input
        placeholder="New Price"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />

      <button onClick={handleUpdate}>Update</button>
    </div>
  );
}

export default EditProduct;