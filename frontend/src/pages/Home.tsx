import {FC, FormEvent, useState} from 'react';
import reactLogo from '../assets/react.svg';
import {getUppercaseText} from "../api/uppercase";
import './Home.scss';

interface HomeProps {

}

const Home: FC<HomeProps> = () => {
  const [textInput, setTextInput] = useState("");
  const [output, setOutput] = useState("");

  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    getUppercaseText(textInput).then(res => {
      setOutput(res.data.text);
    }).catch(err => console.log(err));
  };

  return (
    <div className="App">
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src="/vite.svg" className="logo" alt="Vite logo"/>
        </a>
        <a href="https://reactjs.org" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo"/>
        </a>
      </div>
      <h1>django-react-docker-heroku-template</h1>
      <div className="card">
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <form onSubmit={handleSubmit}>
        <p>Test connection with API:</p>
        <label htmlFor="char-input">Make this text uppercase: </label>
        <input
          id="char-input" type="text" value={textInput}
          onChange={(e) => setTextInput(e.target.value)}
        />
        <button>Submit</button>
        <h3>{output}</h3>
      </form>
    </div>
  );
}

export default Home;
