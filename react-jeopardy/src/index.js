import React from 'react';
import ReactDOM from 'react-dom';
import {Provider} from "react-redux";
import {createStore, applyMiddleware} from "redux";
// import thunk from "redux-thunk";
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import {jeopardy, defaultState} from "./reducers/index";

const store = createStore(jeopardy, defaultState)

ReactDOM.render(
  <Provider store = {store}>
    <App />
  </Provider>,
  document.getElementById('root')
);

serviceWorker.unregister();
