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
      <h3>Search Product</h3>

      <input onChange={(e) => setBarcode(e.target.value)} placeholder="Barcode" />
      <button onClick={search}>Search</button>

      {product && (
        <div>
          <p>Name: {product.product_name}</p>
          <p>Brand: {product.brand}</p>
          <p>Categories: {product.categories}</p>
        </div>
      )}
    </div>
  );
}

export default ProductSearch;