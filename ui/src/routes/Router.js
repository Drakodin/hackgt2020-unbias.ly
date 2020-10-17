import React from 'react';
import { Switch, Route } from 'react-router-dom'
import { Home } from '../home';
import NewsDisplay from '../news/NewsDisplay';

const Router = () => {
    return (
        <Switch>
            <Route exact path='/' component={Home}/>
            <Route exact path='/news' component={NewsDisplay}/>
        </Switch>
    )
}
export default Router;