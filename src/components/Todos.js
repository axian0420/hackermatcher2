import React from 'react';

function Todos() {
  return (
    <div className="center" id="about-box">
      <h1>
        Hacker Matcher
      </h1>

      <img
        alt="gif"
        id="gif"
        src={require("C:/Users/s4rme/.vscode/testapp/src/assets/landing_demo.gif")}
      />

      <h2>
        Meet your perfect team
      </h2>

      <button className="btn btn-success" id="scrollToSignup">
        Try Hacker Matcher
      </button>

    </div>
  );
}

export default Todos;
