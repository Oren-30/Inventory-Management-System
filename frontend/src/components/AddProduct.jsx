import { useState } from "react";
import api from "../api";

function AddProduct() {
  const [barcode, setBarcode] = useState("");
  const [quantity, setQuantity] = useState("");
  const [price, setPrice] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    await api.post("/inventory", {
      barcode,
      quantity: Number(quantity),
      price: Number(price),
    });

    alert("Item added!");
  };

  return (
    <div>
      <h3>Add Product</h3>

      <form onSubmit={handleSubmit}>
        <input placeholder="Barcode" onChange={(e) => setBarcode(e.target.value)} />
        <input placeholder="Quantity" onChange={(e) => setQuantity(e.target.value)} />
        <input placeholder="Price" onChange={(e) => setPrice(e.target.value)} />
        <button type="submit">Add</button>
      </form>
    </div>
  );
}

export default AddProduct;