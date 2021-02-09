import React from 'react';
import PropTypes from 'prop-types';

const Comic = (props) => {
  const { comic, className } = props;
  const img = comic.cdn === '' ? comic.image : comic.cdn
  const images = img.split(' ')
  return (
    <div className={className}>
      <a href={comic.source}>
        {images.map(x => (<img
          className="img-responsive"
          src={x}
          alt={comic.title} title={comic.title}
        />))}
      </a>
    </div>
  );
};

Comic.propTypes = {
  comic: PropTypes.object.isRequired,
  className: PropTypes.string,
};

export default Comic;
