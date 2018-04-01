import q from 'query-string';

export const REQUEST_COMICS = 'REQUEST_COMICS';
export const RECEIVE_COMICS = 'RECEIVE_COMICS';
export const REQUEST_SITES = 'REQUEST_SITES';
export const RECEIVE_SITES = 'RECEIVE_SITES';

export function requestComics(page) {
  return {
    type: REQUEST_COMICS,
    page,
  }
}

export function receiveComics(comics) {
  return {
    type: RECEIVE_COMICS,
    comics,
  }
}

export function fetchComics(page=1, query={}) {
  return dispatch => {
    dispatch(requestComics(page));

    return fetch(`/api/v1/comics/?page=${page}&${q.stringify(query)}`, {
      accept: 'application/json',
    }).then((response) => response.json())
      .then((data) => {
        dispatch(receiveComics(data));
      });
  }
}

export function requestSites() {
  return {
    type: REQUEST_SITES,
  }
}

export function receiveSites(sites) {
  return {
    type: RECEIVE_SITES,
    sites: sites,
  }
}

export function fetchSites() {
  return dispatch => {
    dispatch(requestSites());

    return fetch('/api/v1/comics/sites/')
      .then((response) => response.json())
      .then((data) => {
        dispatch(receiveSites(data));
      });
  };
}
