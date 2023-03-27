import React from "react";
import { useNavigate } from "react-router-dom";

function ErrorPage() {
    let navigate = useNavigate();
    return (
    <div>
        <h1>ERROR! Page not found, please go to a valid page.</h1>
        <br />
        <button onClick={() => {navigate("/")}}>Go back to the home page</button>
    </div>
    );
}

export default ErrorPage;