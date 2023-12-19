import React from 'react';
import './style1.css'

function Content({ value }) {
  const { que, res } = value;

  // Check if response has an error
  if (res && res.error) {
    return <div>Error: {res.error}</div>;
  }

  // Render content normally
  return (
    <div>
      <p>Query: {que}</p>
      <p>Response: {res ? res.data : 'Loading...'}</p>
    </div>
  );
}

export default Content;
