import { useState } from "react";
import api from "../api";

function AddProduct() {

    const [barcode, setBarcode] = useState("");
    const [quantity, setQuantity] = useState("");
    const [price, setPrice] = useState("");

    const submit = async (e) => {

        e.preventDefault();

        await api.post("/inventory", {
            barcode,
            quantity,
            price
        });

        alert("Item Added");

        setBarcode("");
        setQuantity("");
        setPrice("");
    };

    return (

        <form onSubmit={submit}>

            <h2>Add Product</h2>

            <input
                placeholder="Barcode"
                value={barcode}
                onChange={(e) => setBarcode(e.target.value)}
            />

            <input
                placeholder="Quantity"
                value={quantity}
                onChange={(e) => setQuantity(e.target.value)}
            />

            <input
                placeholder="Price"
                value={price}
                onChange={(e) => setPrice(e.target.value)}
            />

            <button>Add Product</button>

        </form>

    );
}

export default AddProduct;