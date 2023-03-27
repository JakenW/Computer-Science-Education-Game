import React from 'react';
import {Routes, Route} from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css"

import Navbar from "./components/navbar.component"
import Home from "./components/Home";
import CreateUser from "./components/CreateUser";
import CreateQuestion from './components/CreateQuestion';
import Play from "./components/Play"
import ErrorPage from "./components/ErrorPage"

function App() {
  return (
    <div className="App">
    <div classname="container">
    <Navbar />
      <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/user" element={<CreateUser />} />
      <Route path="/question" element={<CreateQuestion />} />
      <Route path="/play" element={<Play />} />
      <Route path="*" element={<ErrorPage />} />
      </Routes>
    </div>
    </div>
  );
}

export default App;
