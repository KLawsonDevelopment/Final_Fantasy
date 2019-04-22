import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom'
import './App.css';
import Characters from './components/Characters';
import CharacterGear from './components/CharacterGear';

class App extends Component {
  render() {
    return (
      <Router>
        <div className="App">
          <img src="https://cdn.discordapp.com/attachments/404735741936009216/569946505847242759/ffxiv_04152019_170228_055.png" alt="FC logo" /><h1>Legacy Needs List</h1>
          <div><Link to='/' className="characters">Characters</Link></div>
        </div>

        <Switch>
          <Route exact path='/' component={Characters}></Route>
          <Route path='/character/:id' component={CharacterGear}></Route>
        </Switch>
      </Router>
    );
  }
}

export default App;
