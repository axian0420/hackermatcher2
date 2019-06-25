import React from "react";
import "./Home.css";
import HomePt1 from "../components/HomePt1";
import Header from '../components/Header';

export default class Home extends React.Component {
  render() {
    return (
      <div class="Home">
      <Header/>
      <HomePt1/>
      </div>
    )
  }
}