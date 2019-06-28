import React from 'react';
import { withRouter } from 'react-router-dom';
import SignupForm from './SignupForm'

class Pt4 extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
        firstName: "",
        lastName: "",
        email: "",
        password: "",
        confirmPassword: ""
    };
  }

render() {
  return (
    <div className="center">
      <div className="pt4"  >
        <div className="register-box">
            <h1>Sign up</h1>
            <br></br>
            
            <SignupForm/>

        </div>
      </div>
    </div>
  );
}

handleChange = event => {
  this.setState({
    [event.target.name]: event.target.value
  });
};

handleSubmit = event => {
  event.preventDefault();
  console.log("Submitting");
  console.log(this.state);
  this.props.history.push("/register");
};

}

export default withRouter(Pt4);