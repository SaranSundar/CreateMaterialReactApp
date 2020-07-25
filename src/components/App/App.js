import React, {Fragment} from 'react';
import './App.css';
import {Route, Switch} from "react-router-dom";
import Home from "../Home/Home";
import CssBaseline from "@material-ui/core/CssBaseline";
import SignInSide from "../SignInSide/SignInSide";

function App() {
    return (
        <Fragment>
            <CssBaseline/>
            <Switch>
                <Route exact path="/" component={Home}/>
                <Route exact path="/sign-in" component={SignInSide}/>
            </Switch>
        </Fragment>
    );
}

export default App;
