import React from 'react';
import { Provider } from 'react-redux';
import configureMockStore from 'redux-mock-store'
import thunk from 'redux-thunk'
import { MemoryRouter } from 'react-router-dom';
import { mount } from 'enzyme';
import expect from 'expect';
import SiteView from "../SiteView";

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);


describe('SiteView', () => {
  const store = mockStore({
    sites: {
      sites: [{site: 'foo'}, {site: 'bar'}],
    }
  });
  const wrapper = mount(
    <MemoryRouter>
      <Provider store={store}>
        <SiteView />
      </Provider>
    </MemoryRouter>);

  it('render success', () => {
    expect(wrapper.find('li').length).toEqual(2);
    const aTags = wrapper.find('li a');
    const links = aTags.map((link) => (
      {
        href: link.prop('href'),
        text: link.text(),
      }
    ));
    expect(aTags.length).toEqual(2);
    expect(links).toEqual([
      {
        href: '/?site=foo',
        text: 'foo',
      },
      {
        href: '/?site=bar',
        text: 'bar',
      },
    ]);
  })
});
