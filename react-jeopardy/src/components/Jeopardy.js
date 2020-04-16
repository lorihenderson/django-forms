import React, { Component } from 'react';
// import {connect} from "react";
// import * as JeopardyActions from "../actions/index";
import GameBoard from "./jeopardy/GameBoard";
// import {bindActionCreators} from "redux";
import AnswerForm from "./jeopardy/AnswerForm";
// import JeopardyService from '../jeopardyService';

class Jeopardy extends Component {

  //set our initial state and set up our service as this.client on this component
  constructor(props){
    super(props);
    this.state = {
      score: 0,
      answer: "",
    }
  }

  //when the component mounts, get the first question
  // componentDidMount() {
  //   this.props.getQuestion();
  // }

  checkAnswer = (answer) => {
    if (answer.toUpperCase() === this.state.data.answer.toUpperCase()) {
      this.setState((state, props) => ({
        score: state.score + state.data.value
      }));
    } else {
      this.setState((state, props) => ({
        score: state.score - state.data.value
      }));
    }
    this.getNewQuestion();
  }

  //display the results on the screen
  render() {

    return (
      <div className = "Jeopardy">
        {console.log(this.props.category)
}
        <GameBoard
          // question = {this.props.question}
          // category = {this.props.category}
          // pv = {this.props.pointValue}
          // checkAnswer = {this.checkAnswer}
          // score = {this.state.score}
          // handleAnswer = {this.handleAnswer}
          // handleChange = {this.handleChange}
        />
        {JSON.stringify(this.props.answeredQuestions)}
      </div>
    );
  }
}

export default Jeopardy;


// const mapStateToProps = (state) => ({
//   question: state.question,
//   score: state.score,
//   category: state.category,
//   pointValue: state.pointValue,
//   solution: state.solution,
//   answeredQuestions: state.answeredQuestions
// })

// const mapDispatchToProps = (dispatch) => {
//   return bindActionCreators(JeopardyActions, dispatch)
// }

// export default connect(mapStateToProps, mapDispatchToProps)(Jeopardy);

//https://jservice.kenzie.academy/api/  --> use in fetch