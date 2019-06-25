import React from "react";
import { Route, Switch } from "react-router-dom";
import Landing from "./pages/Landing";
import Registration from "./pages/Registration";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";

export default () =>
  <Switch>
    <Route path="/" exact component={Landing} />
    <Route path="/register" exact component={Registration} />
    <Route path="/home" exact component={Home} />
    <Route component={NotFound} />
  </Switch>;