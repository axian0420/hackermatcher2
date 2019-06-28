import RegPt1 from '../components/RegPt1.js';
import Header from '../components/Header.js';
import React, {Component} from 'react';
import "./Registration.css";

class Registration extends Component {
    render() {
        return (
            <div className = "Registration">
                <Header/>
                <RegPt1/>
            </div>
        );
    }
}

export default Registration;