import React from 'react';
import { Provider } from 'react-redux';
import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
import { MemoryRouter } from 'react-router-dom';
import { shallow, mount } from 'enzyme';
import fetchMock from 'fetch-mock';
import expect from 'expect';
import ComicView from "../ComicView";
import ComicList from "../components/ComicList";
import Page from "../components/Page";
import * as actions from "../actions";

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);


describe('ComicView', () => {
  const comics = [
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
  ];
  const store = mockStore({
    comics: {
      comics: comics,
    }
  });
  const wrapper = mount(
    <MemoryRouter initialEntries={[ '/' ]}>
      <Provider store={store}>
        <ComicView/>
      </Provider>
    </MemoryRouter>);

  it('render success', () => {
    expect(wrapper.find(ComicList).length).toEqual(1);
    const comicList = wrapper.find(ComicList).first();
    expect(comicList.prop('comics')).toEqual(comics);

    expect(wrapper.find(Page).length).toEqual(2);
    const comicView = wrapper.find(ComicView).first();
  })
});
