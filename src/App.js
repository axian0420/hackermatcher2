import React, {Component} from 'react';
import './App.css';
import Todos from './components/Todos';
import Pt2 from './components/Pt2';
import Pt3 from './components/Pt3';
import Pt4 from './components/Pt4.js';
import NavigationBar from './components/NavigationBar';

class App extends Component {
  render() {
    return (
      <div className="App">

        <NavigationBar />
        <Todos />
        <Pt2 />
        <Pt3 />
        <Pt4 />

      </div>
    );
  }
}

export default App;