// import request from "superagent";
const request = require("superagent")
 
const getQuestionAction = (question) => ({
    type: "GET_QUESTION",
    question: question
});

export const answeredQuestion = (question, previousScore, newScore) => dispatch => (
    dispatch({
    type: "ANSWERED_QUESTION",
    question: question,
    previousScore: previousScore,
    newScore: newScore
}))

export const getQuestions = () => dispatch => {
    request
    .get("https://jservice.kenzie.academy/api/random-clue")
    .then ((res) => {
        dispatch(getQuestionAction(res.body))
    })
    .catch((err) => {
        throw new err
    })
}