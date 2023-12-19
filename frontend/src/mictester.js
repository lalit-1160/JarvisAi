import React from 'react';
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function MicTester(){
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
          const fetchData = async () => {
          try {
          const response = await axios.get('http://127.0.0.1:2000/microphone');
          console.log(response.data);
          setData(response.data.result);
    }catch (error){
          setError(`Error: ${error.message}`);
      }
    };
    fetchData();
  }, []);

    return(
    <>
    {data}
    {error}
    </>
    )
}

export default MicTester;