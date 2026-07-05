import { useState } from "react";
import api from "../api";

function ProductSearch() {

    const [barcode, setBarcode] = useState("");

    const [product, setProduct] = useState(null);

    const search = async () => {

        const res = await api.get(`/product/${barcode}`);

        setProduct(res.data);
    };

    return (

        <div>

            <h2>Search OpenFoodFacts</h2>

            <input
                value={barcode}
                onChange={(e) => setBarcode(e.target.value)}
                placeholder="Barcode"
            />

            <button onClick={search}>
                Search
            </button>

            {product && (

                <div className="card">

                    <h3>{product.product_name}</h3>

                    <p>Brand: {product.brand}</p>

                    <p>{product.ingredients}</p>

                    <p>{product.categories}</p>

                    <p>{product.nutrition_grade}</p>

                    <img
                        src={product.image}
                        width="150"
                        alt={product.product_name}
                    />

                </div>

            )}

        </div>

    );
}

export default ProductSearch;