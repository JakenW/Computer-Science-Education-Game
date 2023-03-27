const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');

require('dotenv').config();

const app = express();
const port = process.env.PORT || 3001;

app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.use(cors());

const uri = process.env.ATLAS_URI;
mongoose.connect(uri, { useNewUrlParser: true }
);

const connection = mongoose.connection;
connection.once('open', () => {
  console.log("MongoDB database connection established successfully");
})

const userRouter = require('./routes/users');
const questionsRouter = require('./routes/questions')

app.use('/users', userRouter);
app.use('/questions', questionsRouter);

app.listen(port, () => {
    console.log(`Server is running on port: ${port}`);
})

//was at 22 min