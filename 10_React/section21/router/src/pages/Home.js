import { Link, useNavigate } from "react-router-dom";

function HomPage() {
  const navigate = useNavigate();

  function navigateHandler() {
    navigate("/products");
  }

  return (
    <>
      <h1>Home</h1>
      <p>
        Go to <Link to="/products">the linst of products</Link>.
      </p>
      <p>
        <button onClick={navigateHandler}>Navigate</button>
      </p>
    </>
  );
}

export default HomPage;
