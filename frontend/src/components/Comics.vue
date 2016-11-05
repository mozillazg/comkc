<template>
  <div>
    <!-- Pagination -->
    <div class="row text-center">
      <div class="col-lg-12">
        <ul class="pager">
          <li class="previous">
            <router-link :to="routeObject('prePage')">Previous</router-link>
          </li>
          <li class="next">
            <router-link :to="routeObject('nextPage')">Next</router-link>
          </li>
        </ul>
      </div>
    </div>
    <!-- /.row -->

    <div >
      <!-- Projects Row -->
      <div class="row">
        <div class="col-md-3 portfolio-item" v-for="comic in comics">
          <a :href="comic.source">
            <img class="img-responsive" :src="comic.cdn === '' ? comic.image : comic.cdn"
             :alt="comic.title" :title="comic.title">
          </a>
        </div>
      </div>
      <!-- /.row -->
    </div>

    <hr>

    <!-- Pagination -->
    <div class="row text-center">
      <div class="col-lg-12">
        <ul class="pager">
          <li class="previous">
            <router-link :to="routeObject('prePage')">Previous</router-link>
          </li>
          <li class="next">
            <router-link :to="routeObject('nextPage')">Next</router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import jQuery from 'jquery'
import pageMixin from '../mixins/page'

export default {
  name: 'Comics',
  mixins: [pageMixin],
  data: function () {
    return {
      comics: [],
      random: '',
      page: 1
    }
  },
  created: function () {
    this.fetchData()
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    getQueryParams: function () {
      var random = this.random
      var params = {'page': this.page}
      if (random) {
        params.random = random
      }
      return params
    },
    fetchData: function () {
      this.fetch()
    },
    fetch: function () {
      this.random = this.$route.query.random
      this.page = this.currentPage()
      var url = '/api/v1/comics/?' + jQuery.param(this.getQueryParams())
      this.$http.get(url).then(function (response) {
        // set data on vm
        this.comics = response.body
      })
    },
    routeObject: function (action) {
      var query = {}
      if (this.random) {
        query.random = this.random
      }

      if (action === 'nextPage') {
        query.page = this.nextPage()
        return {name: 'comics', query: query}
      } else if (action === 'prePage') {
        query.page = this.prePage()
        return {name: 'comics', query: query}
      }
    }
  }
}
</script>
