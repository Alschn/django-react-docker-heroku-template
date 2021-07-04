import React, {useState} from 'react';
import logo from '../logo.svg';
import './App.scss';
import axios from "axios";

function App() {
  const [textInput, setTextInput] = useState<string>("");
  const [output, setOutput] = useState<string>("");

  const handleSubmit = () => {
    axios.get(`/api/test?text=${textInput}`).then(res => {
      setOutput(res.data.text);
    }).catch(err => console.log(err));
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo"/>
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

        <div>
          <label htmlFor='char-input'>Make this text uppercase: </label>
          <input
            id='char-input' type='text' value={textInput}
            onChange={(e) => setTextInput(e.target.value)}
          />
          <button onClick={handleSubmit}>Submit</button>
          <h3>{output}</h3>
        </div>
      </header>
    </div>
  );
}

export default App;
