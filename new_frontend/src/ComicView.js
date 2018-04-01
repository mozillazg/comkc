import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import qs from 'query-string'
import _ from 'underscore';
import ComicList from './components/ComicList';
import Page from './components/Page';
import { fetchComics }from './actions';

class ComicView extends Component {

  static propTypes = {
    onLoad: PropTypes.func.isRequired,
    location: PropTypes.object.isRequired,
    comics: PropTypes.array.isRequired,
  };

  state = {
    query: {
      page: 1,
    },
  };

  componentDidMount() {
    this.handleOnLoad(this.props.location);
  }

  componentWillReceiveProps(nextProps) {
    const query = this.parseSearch(nextProps.location);
    if (!_.isEqual(query, this.state.query)) {
      this.handleOnLoad(nextProps.location);
    }
  }

  handleOnLoad = (location) => {
    const query = this.parseSearch(location);
    this.setState({ query: Object.assign({}, query) });

    const page = query.page;
    delete query['page'];
    this.props.onLoad(page, query);
  };

  parseSearch = (location) => {
    const query = qs.parse(location.search);
    if (query.page) {
      query.page = parseInt(query.page, 10);
    } else {
      query.page = 1;
    }
    return query;
  };

  buildPageURL = (page) => {
    const { query } = this.state;
    const newQuery = Object.assign({}, query, {
      page: page,
    });
    return `/?${qs.stringify(newQuery)}`;
  };

  getPreviousPage = (page) => {
    if (page > 1) {
      page = page - 1;
    }
    return this.buildPageURL(page);
  };

  getNextPage = (page) => {
    return this.buildPageURL(page + 1);
  };

  render() {
    const { comics } = this.props;
    const { page } = this.state.query;
    const pages = (
      <Page
        toPrevious={this.getPreviousPage(page)}
        toNext={this.getNextPage(page)}
      />
    );
    return (
      <div>
        {pages}

        <ComicList comics={comics}/>

        <hr />

        {pages}
      </div>)
  }
}

const mapStateToProps = (state) => {
  return {
    comics: state.comics.comics,
    loading: state.comics.loading,
  }
};

const mapDispatchToProps = (dispatch) => {
  return {
    onLoad: (page, query) => (
      dispatch(fetchComics(page, query))
    ),
  }
};

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(ComicView));
