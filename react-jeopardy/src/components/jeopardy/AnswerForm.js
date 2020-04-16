import React, {Component} from "react";
import Jeopardy from "../Jeopardy";

class AnswerForm extends Component{

    constructor(props) {
        super(props);

        this.state = {
            answer: ""
        }
    }

    handleChange = event => {
        this.setState({
            answer: event.target.value
        });
    }

    handleAnswer = event => {
        event.preventDefault()
        let score = this.state.score
        const answer = this.state.answer
        const solution = this.props.solution

        if (answer === solution) {
            score += this.props.pointValue
        } else {
            score -= this.props.pointValue
        }
        this.props.answeredQuestion(this.props.question, this.state.score, score)
        this.setState({score, answer: ""})
        this.getQuestion()
    }

    handleSubmit = event => {
        event.preventDefault();
        this.props.checkAnswer(this.state.answer);
        this.setState({
            answer: ""
        });
    }
    
    render() {        

        return (
            <div className = "AnswerForm">
                <form onSubmit = {this.handleSubmit}>
                    <input
                        type = "text"
                        name = "answer"
                        placeholder = "Answer"
                        value = {this.state.answer}
                        onChange = {this.handleChange}
                    />
                    <button>Go</button>
                </form>
            </div>
        )
    }
}

export default AnswerForm;