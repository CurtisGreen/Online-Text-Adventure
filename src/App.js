import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {
  const [commands, setCommands] = useState([]);  // List of previous commands
  const [curCommand, setCommand] = useState(''); // Current command

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        
        {/* Show previous commands */}
        {commands.map(command => (
          <p key={Math.random()}>{command}</p>
        ))}
        <input name="text" onChange={(e) => setCommand(e.target.value)} />
        <input type="submit" onClick={() => fetchData(setCommands, curCommand)} />
      </header>
    </div>
  );
}

async function fetchData(setCommands, command) {
  const raw = await fetch('/command', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({'command': command})
  });
  const data = await raw.json();
  console.log(data)
  setCommands(data.commands);
}

export default App;
