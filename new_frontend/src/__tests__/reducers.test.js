import expect from 'expect';
import * as actions from '../actions';
import * as reducers from '../reducers';
import {REQUEST_SITES} from "../actions";
import {RECEIVE_SITES} from "../actions";
import {REQUEST_COMICS} from "../actions";
import {RECEIVE_COMICS} from "../actions";

describe('sites reducers', () => {
  it('should return the initial state', () => {
    expect(reducers.sitesReducer(undefined, {})).toEqual({
      loading: true,
      sites: [],
    });
  });

  it('should handle REQUEST_SITES', () => {
    expect(reducers.sitesReducer({}, {
      type: actions.REQUEST_SITES
    })).toEqual({
      loading: true,
    });
  });

  it('should handle RECEIVE_SITES', () => {
    expect(reducers.sitesReducer({}, {
      type: actions.RECEIVE_SITES,
      sites: [
        {site: 'foo'},
        {site: 'bar'},
      ],
    })).toEqual({
      loading: false,
      sites: [
        {site: 'foo'},
        {site: 'bar'},
      ],
    })
  });
});

describe('comics reducers', () => {
  it('should return initial state', () => {
    expect(reducers.comicsReducer(undefined, {})).toEqual({
      comics: [],
      loading: true,
      page: 1,
    });
  });

  it('should handle REQUEST_COMICS', () => {
    expect(reducers.comicsReducer({}, {
      type: actions.REQUEST_COMICS,
      page: 2,
    })).toEqual({
      loading: true,
      page: 2,
    })
  });

  it('should handle RECEIVE_COMICS', () => {
    expect(reducers.comicsReducer({}, {
      type: actions.RECEIVE_COMICS,
      comics: [
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
    })).toEqual({
      loading: false,
      comics: [
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
    })
  });
});
