import React from "react";
import {Form, Button, Col, FormControl} from 'react-bootstrap';
import { withRouter } from 'react-router-dom';

class SignupForm extends React.Component {
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
        const { firstName, lastName, email, password, confirmPassword } = this.state;
        return (
            <Form onSubmit={this.handleSubmit.bind(this)}>
              <Form.Row>
                <Form.Group as={Col} controlId="formFirstName">
                <FormControl 
                name="firstName"
                type = "text"
                placeholder="First Name"
                value={firstName}
                onChange={this.handleChange}
                 />
                </Form.Group>

                <Form.Group as={Col} controlId="formLastName">
                <FormControl 
                name="lastName"
                type = "text"
                placeholder="Last Name"
                value={lastName}
                onChange={this.handleChange}
                 />
                </Form.Group>
              </Form.Row>

              <Form.Group controlId="formEmail">
              <FormControl 
                name="email"
                type = "email"
                placeholder="Email"
                value={email}
                onChange={this.handleChange}
                 />
              </Form.Group>

              <Form.Group controlId="formPassword">
                <FormControl 
                name="password"
                type = "password"
                placeholder="Password"
                value={password}
                onChange={this.handleChange}
                 />
              </Form.Group>

              <Form.Group controlId="formConfirmPassword">
              <FormControl 
                name="confirmPassword"
                type = "password"
                placeholder="Confirm Password"
                value={confirmPassword}
                onChange={this.handleChange}
                 />
              </Form.Group>
              
              <Button variant="success" type="submit">
                Submit
              </Button>
            </Form>
        );
    }

    handleChange = event => {
        this.setState({
          [event.target.name]: event.target.value
        });

       // if (event.target.value.length === 3)
       //   alert('hi');
      };
    
      handleSubmit = event => {
        event.preventDefault();
        console.log("Submitting");
        console.log(this.state);
        this.props.history.push("/register");
      };
    }

    export default withRouter(SignupForm)
