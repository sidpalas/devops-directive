import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Super Simple Static Site Setup w/ SSL (S^6)</p>
        <p>GCS + Cloudflare = 😍🎉</p>
        <a
          className="App-link"
          href="https://devopsdirective.com"
          target="_blank"
          rel="noopener noreferrer"
        >
          DevOps Directive Home
        </a>
      </header>
    </div>
  );
}

export default App;
