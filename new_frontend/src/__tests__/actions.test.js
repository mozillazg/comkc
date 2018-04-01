import configureMockStore from 'redux-mock-store'
import thunk from 'redux-thunk'
import * as actions from '../actions';
import fetchMock from 'fetch-mock'
import expect from 'expect'

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);

describe('sites actions', () => {
  afterEach(() => {
    fetchMock.reset();
    fetchMock.restore();
  });

  it('creates RECEIVE_SITES when fetching sites has been done', () => {
    fetchMock
      .getOnce(
          '/api/v1/comics/sites/',
          {
            body: [{site: 'foo'}, {site: 'bar'}],
            headers: { 'content-type': 'application/json' },
          }
        );

    const expectedActions = [
      { type: actions.REQUEST_SITES },
      { type: actions.RECEIVE_SITES, sites: [{site: 'foo'}, {site: 'bar'}] },
    ];
    const store = mockStore({ sites: [] });

    return store.dispatch(actions.fetchSites()).then(() => {
      expect(store.getActions()).toEqual(expectedActions);
    })
  })
});


describe('comics actions', () => {
  afterEach(() => {
    fetchMock.reset();
    fetchMock.restore();
  });

  it('creates RECEIVE_COMICS when fetching comics has been done', () => {
    fetchMock
      .getOnce(
        '/api/v1/comics/?page=1&',
        {
          body: [
            {
              "uuid": "43e79c40ca90494abc608751ca6d8697",
              "site": "i love you | Twitter",
              "title": "i love you | Twitter: RT @TheFactsBook: Don't ask meow I know this!... https://t.co/RwefNHBjHp",
              "source": "https://twitter.com/TheFactsBook/status/956497470627897344/photo/1",
              "image": "https://pbs.twimg.com/media/DUYpYLkVwAALim9.jpg:large",
              "cdn": "",
              "posted_at": "Sun Jan 28 09:12:30 2018",
              "created_at": "Sun Jan 28 09:15:45 2018"
            },
            {
              "uuid": "60661c0a39ac4ba1a44a6aa6632f1c9e",
              "site": "Guy Kopsombut | Twitter",
              "title": "Guy Kopsombut | Twitter: Oh hai! 4amShower is being spotlighted on the Tapas.io right now! Check it out :) @tapas_app you guys are awesome :) https://t.co/aBl2sNH11l",
              "source": "https://twitter.com/4AMShower/status/892256607450664960/photo/1",
              "image": "https://pbs.twimg.com/media/DGHupZSW0AAreSq.jpg:large",
              "cdn": "",
              "posted_at": "Tue Aug  1 13:32:07 2017",
              "created_at": "Sat Aug  5 07:52:09 2017"
            },
          ],
          headers: { 'content-type': 'application/json' },
        },
      );

    const expectedActions = [
      { type: actions.REQUEST_COMICS, page: 1 },
      { type: actions.RECEIVE_COMICS, comics: [
          {
            "uuid": "43e79c40ca90494abc608751ca6d8697",
            "site": "i love you | Twitter",
            "title": "i love you | Twitter: RT @TheFactsBook: Don't ask meow I know this!... https://t.co/RwefNHBjHp",
            "source": "https://twitter.com/TheFactsBook/status/956497470627897344/photo/1",
            "image": "https://pbs.twimg.com/media/DUYpYLkVwAALim9.jpg:large",
            "cdn": "",
            "posted_at": "Sun Jan 28 09:12:30 2018",
            "created_at": "Sun Jan 28 09:15:45 2018"
          },
          {
            "uuid": "60661c0a39ac4ba1a44a6aa6632f1c9e",
            "site": "Guy Kopsombut | Twitter",
            "title": "Guy Kopsombut | Twitter: Oh hai! 4amShower is being spotlighted on the Tapas.io right now! Check it out :) @tapas_app you guys are awesome :) https://t.co/aBl2sNH11l",
            "source": "https://twitter.com/4AMShower/status/892256607450664960/photo/1",
            "image": "https://pbs.twimg.com/media/DGHupZSW0AAreSq.jpg:large",
            "cdn": "",
            "posted_at": "Tue Aug  1 13:32:07 2017",
            "created_at": "Sat Aug  5 07:52:09 2017"
          },
        ] },
    ];
    const store = mockStore({ comics: [] });

    return store.dispatch(actions.fetchComics()).then(() => {
      expect(store.getActions()).toEqual(expectedActions);
    })
  })
});
