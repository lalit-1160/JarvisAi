import React, { useState,useEffect } from 'react';
import Mic from './image/mic.png';
import SubmitIcon from './image/submit.png';
import Bottom from './bottom';
import QueryHit from './queryhit'; // Make sure to import the QueryHit component
import './style1.css';
import axios from 'axios';

function Query(props) {
  /* input Tag Variable */
  let [inputvalue,setinputvalue] = useState('');


  /* Content Div Variable */
  let [user, setUser] = useState('');

  /* Bottom Div Variable */
  let [data, setData] = useState(false);
  let [msg, setMsg] = useState('');
  let [queryHitValue, setQueryHitValue] = useState(null);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:2000/microphone');
      setinputvalue(response.data.result);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };


  useEffect(() => {
    if (props.value == 3) {
      setinputvalue('What is the Time');
    }
  }, [props.value]);

  function submitFun() {
    doing()
    setMsg('Recognising.........');
  }

  function fun1(event) {
    if (event.key === 'Enter') {
      doing()
    }
  }

  function doing(){
      let s = inputvalue;
      setUser(s);

      let obj = {
        query: { s },
        type:props.value
      };

      // Set the value in the state for conditional rendering
      setQueryHitValue(obj);

      setMsg('Recognising.........');
      setinputvalue('')
  }

  function clickHandler() {
    if (data === false) {
      setMsg('Mic Opened');
      setinputvalue('')
      fetchData();
      setData(true);
    } else {
      setMsg('Mic Closed');
      setData(false);
    }
  }

  const handleInputChange = (event) => {
    setinputvalue(event.target.value);
  };

  return (
    <>
      {/* Conditionally render QueryHit based on the state value */}
      {queryHitValue && <QueryHit value={queryHitValue} />}

      <div id="query-box">
        <input type="text" value={inputvalue} id="input" placeholder="Type your query" onKeyPress={fun1} onChange={handleInputChange} />
        <img src={Mic} id="mic" onClick={clickHandler} />
        <img src={SubmitIcon} id="submit" onClick={submitFun} />
      </div>

      <Bottom Data={msg} />
    </>
  );
}

export default Query;
