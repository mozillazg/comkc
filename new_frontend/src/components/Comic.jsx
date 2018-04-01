import React from 'react';
import PropTypes from 'prop-types';

const Comic = (props) => {
  const { comic, className } = props;
  return (
    <div className={className}>
      <a href={comic.source}>
        <img
          className="img-responsive"
          src={comic.cdn === '' ? comic.image : comic.cdn}
          alt={comic.title} title={comic.title}
        />
      </a>
    </div>
  );
};

Comic.propTypes = {
  comic: PropTypes.object.isRequired,
  className: PropTypes.string,
};

export default Comic;
