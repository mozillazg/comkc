import Vue from 'vue'
import Router from 'vue-router'
import Resource from 'vue-resource'

import App from './App'
import Comics from './components/Comics.vue'
import Sites from './components/Sites.vue'

Vue.use(Router)
Vue.use(Resource)

const routes = [
  {path: '/', name: 'comics', component: Comics, alias: '/comics/'},
  {path: '/sites/', name: 'sites', component: Sites, alias: '/sites/'},
  {path: '*', redirect: '/'}
]

const router = new Router({
  linkActiveClass: 'active',
  routes: routes
})

/* eslint-disable no-new */
new Vue({
  router: router,
  el: 'app',
  render: h => h(App)
})
