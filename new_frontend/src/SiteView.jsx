import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import { fetchSites }from './actions';

class SiteView extends Component {

  static propTypes = {
    onLoad: PropTypes.func.isRequired,
    sites: PropTypes.array.isRequired,
  };

  componentDidMount() {
    this.props.onLoad();
  }

  render() {
    const { sites } = this.props;
    return (
      <div className="row">
        {sites.map(s => (
          <ul key={s.site}>
            <li key={s.site}>
              <Link to={`/?site=${s.site}`} key={s.site}>{s.site}</Link>
            </li>
          </ul>
        ))}
      </div>)
  }
}

const mapStateToProps = (state) => {
  return {
    sites: state.sites.sites,
    loading: state.sites.loading,
  }
};

const mapDispatchToProps = (dispatch) => {
  return {
    onLoad: () => dispatch(fetchSites()),
  }
};

export default connect(mapStateToProps, mapDispatchToProps)(SiteView);
