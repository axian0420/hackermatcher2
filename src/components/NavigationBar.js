import React from 'react';
import {Navbar, Form, FormControl, Button, Nav} from 'react-bootstrap';

function NavigationBar() {
  return (
    <div className="NavBar">
      
      <Navbar fixed="top" bg="light" expand="lg">
        <Navbar.Brand href="/home" >
        <img
        alt=""
        src={require("C:/Users/s4rme/.vscode/testapp/src/assets/favicon.png")}
        width="30"
        height="30"
        className="d-inline-block align-top"
      />
      Hacker Matcher
    </Navbar.Brand>
  <Navbar.Toggle aria-controls="basic-navbar-nav" />
  <Navbar.Collapse id="basic-navbar-nav">
    <Nav className="mr-auto">
    </Nav>
    <Form inline>
      <FormControl type="text" placeholder="Email" className="Email" />
      <FormControl type="text" placeholder="Password" className="Password" />
      <Button variant="outline-success">Login</Button>
    </Form>
  </Navbar.Collapse>
</Navbar>
        </div>
  );
}

export default NavigationBar;