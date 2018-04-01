import { REQUEST_COMICS, RECEIVE_COMICS,
  REQUEST_SITES, RECEIVE_SITES } from './actions';

const comicsInitState = {
  comics: [],
  loading: true,
  page: 1,
};

export function comicsReducer(state=comicsInitState, action) {
  switch (action.type) {
    case REQUEST_COMICS: {
      return Object.assign({}, state, {
        loading: true,
        page: action.page,
      });
    }
    case RECEIVE_COMICS: {
      return Object.assign({}, state, {
        loading: false,
        comics: action.comics,
      });
    }
    default: {
      return state;
    }
  }
}

const sitesInitState = {
  loading: true,
  sites: [],
};

export function sitesReducer(state=sitesInitState, action) {
  switch (action.type) {
    case REQUEST_SITES: {
      return Object.assign({}, state, {
        loading: true,
      })
    }
    case RECEIVE_SITES: {
      return Object.assign({}, state, {
        loading: false,
        sites: action.sites,
      })
    }
    default: {
      return state;
    }
  }
}
