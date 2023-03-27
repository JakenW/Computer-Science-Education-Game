import React from "react";
import {Form, Button} from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import {useState, useEffect} from "react";
import axios from "axios";

function CreateQuestion() {
    const navigate = useNavigate();
    const [question, setQuestion] = useState({
        question:"",
        correctAnswer:"",
        option1:"",
        option2:"",
        option3:"",
        option4:"",
    });

    const handleChange = (event) => {
        const {name, value} = event.target;

        setQuestion(prev => {
            return({
                ...prev,
                [name]: value
            })
        })
    };

    const handleClick = (event) => {
        event.preventDefault();

        //changed this line for testing, took off /add
        axios.post("http://localhost:3001/questions/add", question)
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
            <h3>Create New Question</h3>
            <Form>
                <Form.Group>
                    <Form.Control 
                    name="question" 
                    value={question.question}
                    placeholder="Question" 
                    style={{ marginBottom: "1rem"}}
                    onChange={handleChange}
                    />

                    <Form.Control 
                    name="correctAnswer" 
                    value={question.correctAnswer}
                    placeholder="Correct Answer to Question" 
                    style={{ marginBottom: "1rem"}}
                    onChange={handleChange}
                    />

                    <Form.Control 
                    name="option1" 
                    value={question.option1}
                    placeholder="Possible Answer 1" 
                    style={{ marginBottom: "1rem"}}
                    onChange={handleChange}
                    />

                    <Form.Control 
                    name="option2" 
                    value={question.option2}
                    placeholder="Possible Answer 2" 
                    style={{ marginBottom: "1rem"}}
                    onChange={handleChange}
                    />

                    <Form.Control 
                    name="option3" 
                    value={question.option3}
                    placeholder="Possible Answer 3" 
                    style={{ marginBottom: "1rem"}}
                    onChange={handleChange}
                    />

                    <Form.Control 
                    name="option4" 
                    value={question.option4}
                    placeholder="Possible Answer 4" 
                    style={{ marginBottom: "1rem"}}
                    onChange={handleChange}
                    />
                </Form.Group>
                <Button onClick={handleClick}>Create Question</Button>
            </Form>
        </div>
    );
}

export default CreateQuestion;