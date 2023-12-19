//import React, { useState, useEffect } from 'react';
//import axios from 'axios';
//
//function Msg() {
//  const [data, setData] = useState(null);
//  const [error, setError] = useState(null);
//
//  useEffect(() => {
//    const fetchData = async () => {
//      try {
//        const response = await axios.get('http://127.0.0.1:2000/commands');
//        setData(response.data.message);
//      } catch (error){
//        setError(`Error: ${error.message}`);
//      }
//    };
//
//    fetchData();
//  }, []);
//
//
//  return (
//    <div>
//      <h1>React App</h1>
//      {error && <p>{error}</p>}
//      {data && <p>{data}</p>}
//    </div>
//  );
//}
//
//export default Msg;
