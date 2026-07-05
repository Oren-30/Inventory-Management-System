import api from "../api";

function DeleteProduct({ id, refresh }) {

    const remove = async () => {

        await api.delete(`/inventory/${id}`);

        refresh();
    };

    return (
        <button onClick={remove}>
            Delete
        </button>
    );
}

export default DeleteProduct;