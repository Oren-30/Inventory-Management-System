import { useEffect, useState } from "react";
import api from "../api";
import DeleteProduct from "./DeleteProduct";
import EditProduct from "./EditProduct";

function InventoryList() {

    const [items, setItems] = useState([]);

    const loadInventory = () => {
        api.get("/inventory")
            .then((res) => setItems(res.data))
            .catch(console.error);
    };

    useEffect(() => {
        loadInventory();
    }, []);

    return (
        <div>

            <h2>Inventory</h2>

            {items.map((item) => (

                <div key={item.id} className="card">

                    <h3>{item.product_name}</h3>

                    <p>Brand: {item.brand}</p>

                    <p>Barcode: {item.barcode}</p>

                    <p>Quantity: {item.quantity}</p>

                    <p>Price: KES {item.price}</p>

                    <EditProduct
                        item={item}
                        refresh={loadInventory}
                    />

                    <DeleteProduct
                        id={item.id}
                        refresh={loadInventory}
                    />

                </div>

            ))}

        </div>
    );
}

export default InventoryList;