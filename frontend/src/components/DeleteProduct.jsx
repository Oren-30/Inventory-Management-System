import { useState } from "react";
import api from "../api";

function DeleteProduct() {
  const [id, setId] = useState("");

  const handleDelete = async () => {
    if (!id) {
      alert("Please enter item ID");
      return;
    }

    try {
      await api.delete(`/inventory/${id}`);
      alert("Item deleted successfully!");
      setId("");
    } catch (err) {
      alert("Error deleting item");
    }
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h3>Delete Product</h3>

      <input
        placeholder="Item ID"
        value={id}
        onChange={(e) => setId(e.target.value)}
      />

      <button onClick={handleDelete} style={{ background: "red", color: "white" }}>
        Delete
      </button>
    </div>
  );
}

export default DeleteProduct;