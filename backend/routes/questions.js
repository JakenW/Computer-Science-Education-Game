const router = require('express').Router();
let Question = require('../models/question.model');

router.route('/').get((req, res) => {
    Question.find()
    .then(questions => res.json(questions))
    .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/add').post((req, res) => {
    const question = req.body.question;
    const correctAnswer = req.body.correctAnswer;
    const option1 = req.body.option1;
    const option2 = req.body.option2;
    const option3 = req.body.option3;
    const option4 = req.body.option4;

    const newQuestion = new Question({
        question,
        correctAnswer,
        option1,
        option2,
        option3,
        option4,
    });

    newQuestion.save()
    .then(() => res.json('Question added!'))
    .catch(err => res.status(400).json('Error: ' + err));
});

module.exports = router;

//around 34 minutes in video, currently trying to troubleshoot question crud not working
