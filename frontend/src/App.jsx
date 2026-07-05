import Navbar from "./components/Navbar";
import AddProduct from "./components/AddProduct";
import InventoryList from "./components/InventoryList";
import ProductSearch from "./components/ProductSearch";

function App() {
  return (
    <>
      <Navbar />

      <div className="container">
        <AddProduct />
        <ProductSearch />
        <InventoryList />
      </div>
    </>
  );
}

export default App;