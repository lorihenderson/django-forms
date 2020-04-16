const defaultState = {
    question: "",
    score: 0, 
    category: "",
    pointValue: 0,
    solution: "",
    answerQuestions: []
}

const jeopardy = (state = defaultState, action) => {
    switch(action.type) {
        case "GET_QUESTION":
            const newQuestionState = {
                question: action.question.question,
                pointValue: action.question.vaue,
                category: action.question.category && action.question.category.title || "",
                solution: action.question.answer
            }
            return Object.assign({}, state, newQuestionState)
        case "ANSWERED_QUESTIONS":
            const answerQuestionState = {
                question: action.question,
                pointValue: action.pointValue,
                category: action.category,
                solution: action.solution,
                answer: action.answer,
                previouaScore: action.previousScore,
                newScore: action.newScore
            }
            state.answerQuestions.push(answerQuestionState)
            return Object.assign({}, state)

        default:
            return state
    }
}

export {jeopardy, defaultState}



// export const FETCH_QUESTION = "FETCH_QUESTION";
// export const UPDATE_SCORE = "UPDATE_SCORE";
// export const GET_CATEGORIES = "GET_CATEGORIES";

// const defaultState = {
//     score: 0, 
//     categories: "", 
//     questions: ""
// }

// const jeopardy = (state = defaultState, action) => {
//     switch(action.type) {
//         case FETCH_QUESTION:
//             return {...state, questions: action.questions};

//         case UPDATE_SCORE:
//             return {...state, score: action.score + state.score}
        
//         case GET_CATEGORIES:
//             return {...state, categories: action.categories};
            
//         default:
//             return state
//     }
// }

// ////action creators that the dispatch will use as a parameter ex: dispatch(updateScore(20))
// function getQuestions(questions) { //make into an arrow function
//     return {type: FETCH_QUESTION, questions: questions}
// }

// const updateScore= score=>({ 
//     type: UPDATE_SCORE,
//     score: score

// })

// const getCategories = categories => ({
//     type: GET_CATEGORIES,
//     categories: categories
// })

// export default {jeopardy, defaultState}


// //write async operations ex: Promises and .then() and dispatching actions with the action creators
