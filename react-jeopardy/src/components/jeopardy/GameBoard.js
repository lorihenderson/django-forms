import React from "react";
import AnswerForm from "./AnswerForm";
import {useSelector} from "react-redux"

function GameBoard(props) {
  // const category = props.data.category && props.data.category.title;

  const data = useSelector(state=>({
    category: state.category,
    pointValue: state.pointValue,
    question: state.question,
    solution: state.solution,
    score: state.score
  }))
  console.log(data)

  return (
    <div className="GameBoard">
      <h2>{data.category}</h2>
      <h3>{data.pointValue}</h3>
      <div className="clue">{data.question}</div>
      <AnswerForm checkAnswer={data.solution} />
      <div className="score">Your winnings: ${data.score}</div>
    </div>
  );
}

export default (GameBoard);
