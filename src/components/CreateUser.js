import React from "react";
import {Form, Button} from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import {useState, useEffect} from "react";
import axios from "axios";

function CreateUser() {
    const navigate = useNavigate();
    const [user, setUser] = useState({
        username:"",
    });

    const handleChange = (event) => {
        const {name, value} = event.target;

        setUser(prev => {
            return({
                ...prev,
                [name]: value
            })
        })
    };

    const handleClick = (event) => {
        event.preventDefault();

        //changed this line for testing, took off /add
        axios.post("http://localhost:3001/users/add", user)
            .then((res) => console.log(res))
            .catch((err) => console.log(err));

        navigate("/");
    }

    /*
    useEffect(() => {
        console.log(user);
    }, [user]);
    */

    return (
        <div>
            <h3>Create New User</h3>
            <Form>
                <Form.Group>
                    <Form.Control 
                    name="username" 
                    value={user.username}
                    placeholder="Username" 
                    style={{ marginBottom: "1rem"}}
                    onChange={handleChange}
                    />
                </Form.Group>
                <Button onClick={handleClick}>Register</Button>
            </Form>
        </div>
    );
}

export default CreateUser;

