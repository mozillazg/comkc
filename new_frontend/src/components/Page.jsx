import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';

class Page extends Component {

  static propTypes = {
    toPrevious: PropTypes.oneOfType([
      PropTypes.string,
      PropTypes.object,
    ]),
    toNext: PropTypes.oneOfType([
      PropTypes.string,
      PropTypes.object,
    ]),
    propsPrevious: PropTypes.object,
    propsNext: PropTypes.object,
  };

  static defaultProps = {
    toPrevious: '',
    toNext: '',
    propsPrevious: {},
    propsNext: {},
  };

  render() {
    return (
      <div className="row text-center">
        <div className="col-lg-12">
          <ul className="pager">
            <li className="previous">
              <Link to={this.props.toPrevious} {...this.props.propsPrevious}>Previous</Link>
            </li>
            <li className="next">
              <Link to={this.props.toNext} {...this.props.propsNext}>Next</Link>
            </li>
          </ul>
        </div>
      </div>)
  }
}

export default Page