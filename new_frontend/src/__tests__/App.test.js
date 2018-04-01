import React from 'react';
import { shallow, mount } from 'enzyme';
import { MemoryRouter } from 'react-router-dom';
import expect from 'expect';
import App from '../App';
import SiteView from "../SiteView";
import ComicView from "../ComicView";

it('renders without crashing', () => {
  shallow(<App />);
});

describe('route test', () => {
  it('should render SiteView on /sites', () => {
    const wrapper = mount(
      <MemoryRouter initialEntries={['/sites']}>
        <App/>
      </MemoryRouter>
    );
    expect(wrapper.find(SiteView).length).toEqual(1);
    expect(wrapper.find(ComicView).length).toEqual(0);
  });

  it('should render ComicView on /', () => {
    const wrapper = mount(
      <MemoryRouter initialEntries={['/']}>
        <App/>
      </MemoryRouter>
    );
    expect(wrapper.find(SiteView).length).toEqual(0);
    expect(wrapper.find(ComicView).length).toEqual(1);
  });

  it('should render ComicView on /foo', () => {
    const wrapper = mount(
      <MemoryRouter initialEntries={['/foo']}>
        <App/>
      </MemoryRouter>
    );
    expect(wrapper.find(SiteView).length).toEqual(0);
    expect(wrapper.find(ComicView).length).toEqual(1);
  });
});
