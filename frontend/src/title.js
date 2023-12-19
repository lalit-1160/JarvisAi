import React,{useState} from 'react';
import './style1.css';
import Query from './query';

function Title(){
     let [selectValue,setValue] = useState('');

     function eventHandler(event){
       console.log(event.target.value);
        setValue(event.target.value);
     }
      return(
         <>
         <div id="title">
            Jarvis - OpenAi + Python Powered AI Assistance
            <select id="list" onChange={eventHandler}>

                     <option value="0">Chat GPT</option>
                     <option value="1">Open Browser</option>
                     <option value="2">Open Application</option>
                     <option value="3">Time</option>

            </select>
         </div>

         <Query value={selectValue}/>

         </>
      );
}

export default Title;