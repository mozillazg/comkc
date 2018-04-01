import React, { Component } from 'react';
import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import { Provider } from 'react-redux';
import { Route, Redirect, Switch } from 'react-router-dom';
import './App.css';
import { comicsReducer, sitesReducer } from './reducers';
import ComicView from './ComicView';
import SiteView from './SiteView';

const reducer = combineReducers({
  comics: comicsReducer,
  sites: sitesReducer,
});

const store = createStore(
  reducer,
  applyMiddleware(thunk),
);

class App extends Component {
  render() {
    return (
      <div >
        <div >
          <Switch>
            <Route exact path="/sites" component={SiteView} />
            <Route exact path="/" component={ComicView} />
            <Redirect to="/" />
          </Switch>
        </div>
      </div>
    );
  }
}

const WrappedApp = () => (
  <Provider store={store}>
    <App/>
  </Provider>
);
export default WrappedApp;
