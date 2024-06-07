import React from 'react';
import { useParams } from 'react-router-dom';

function User() {
  const { usr } = useParams();

  return (
    <div>
      <h1>User Component</h1>
      <p>User ID: {usr}</p>
    </div>
  );
}

export default User;
