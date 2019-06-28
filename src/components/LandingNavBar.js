import React from 'react';
import {Navbar, Nav} from 'react-bootstrap';
import MyForm from './MyForm';

class NavigationBar extends React.Component {

  render() {
    return (
          <div className="NavBar">
            <Navbar fixed="top" bg="light" expand="lg">
              <Navbar.Brand href="/">
              <img
              alt=""
              src={require("../assets/favicon.png")}
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
                <MyForm/>
                
              </Navbar.Collapse>
            </Navbar>
          </div>
    );
  }
}

export default NavigationBar;


// import React from 'react';
// import {Navbar, Form, Nav, Button, FormControl} from 'react-bootstrap';

// class NavigationBar extends React.Component {

//   state = {email: "a", password: "s"};

//   handleClick = (event) => {
//     event.preventDefault()
//     this.setState({email : this.textInput.value});// email
//     this.setState({ password :  this.passInput.value});// password
//     console.log(this.state.email)
//     console.log(this.state.password) 
//   }

//   render() {
//     return (
//           <div className="NavBar">
//             <Navbar fixed="top" bg="light" expand="lg">
//               <Navbar.Brand href="/home"  >
//               <img
//               alt=""
//               src={require("../assets/favicon.png")}
//               width="30"
//               height="30"
//               className="d-inline-block align-top"
//             />
//             Hacker Matcher
//               </Navbar.Brand>
              
//               <Navbar.Toggle aria-controls="basic-navbar-nav" />
//               <Navbar.Collapse id="basic-navbar-nav">
//                 <Nav className="mr-auto">

//                 </Nav>
//                 <Form inline onSubmit={this.handleClick}>
//                   <FormControl type="text" placeholder="Email" className="Email" ref={(input) => { this.textInput = input; }}/>
//                   <FormControl type="text" placeholder="Password" className="Password" ref={(pass) => { this.passInput = pass; }}/>
//                   <Button type="submit">Login</Button>
//                 </Form>

//               </Navbar.Collapse>
//             </Navbar>
//           </div>
//     );
//   }
// }

// export default NavigationBar;