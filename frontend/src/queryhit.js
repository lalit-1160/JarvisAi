import React, { useState, useEffect } from 'react';
import axios from 'axios';
//import Content from './content';
import './style1.css'

function QueryHit(props) {
  const [response, setResponse] = useState('');
  const [quer,setQuer] = useState('')

  useEffect(() => {

    const fetchData = async () => {
      try {
        const result = await axios.post('http://127.0.0.1:2000/data', {
          query: props.value.query.s,
          type: props.value.type
        });

        setQuer("Query : "+props.value.query.s)
        console.log(result.data);
        setResponse("Response : "+result.data.result);
      } catch (error) {
        console.error("Error", error);
      }
    };

    fetchData();
  }, [props.value.query.s]); // Only re-run the effect if props.value.query.s changes

  return (
    <div id='main'>
        <p>{quer}</p>
        <p>{response}</p>
    </div>
  );
}

export default QueryHit;
