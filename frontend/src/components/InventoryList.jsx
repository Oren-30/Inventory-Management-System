import { useEffect, useState } from "react";
import api from "../api";

function InventoryList() {
  const [items, setItems] = useState([]);

  const loadItems = async () => {
    const res = await api.get("/inventory");
    setItems(res.data);
  };

  useEffect(() => {
    loadItems();
  }, []);

  return (
    <div>
      <h3>Inventory</h3>
      {items.map((item) => (
        <div key={item.id} style={{ border: "1px solid #ccc", margin: 5, padding: 5 }}>
          <p>{item.product_name}</p>
          <p>{item.brand}</p>
          <p>Qty: {item.quantity}</p>
          <p>Price: {item.price}</p>
        </div>
      ))}
    </div>
  );
}

export default InventoryList;