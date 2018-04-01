import React from 'react';
import PropTypes from 'prop-types';
import Comic from './Comic';

const ComicList = (props) => {
  const comics = props.comics.map((c) => {
    return <Comic key={c.uuid} comic={c} className="col-md-3 portfolio-item"/>
  });
  return (
    <div className="row">
    {comics}
    </div>
  );
};

ComicList.propTypes = {
  comics: PropTypes.array.isRequired,
};

export default ComicList;