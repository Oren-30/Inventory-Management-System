import api from "../api";

function EditProduct({ item, refresh }) {

    const edit = async () => {

        const quantity = prompt("Quantity", item.quantity);

        const price = prompt("Price", item.price);

        await api.patch(`/inventory/${item.id}`, {
            quantity,
            price
        });

        refresh();
    };

    return (
        <button onClick={edit}>
            Edit
        </button>
    );
}

export default EditProduct;