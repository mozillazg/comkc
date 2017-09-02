<template>
  <div>

    <div >
      <!-- Projects Row -->
      <div class="row">
        <ul v-for="site in sites">
          <li>
            <a :href="site.url">
            {{ site.site }}
            </a>
          </li>
        </div>
      </div>
      <!-- /.row -->
    </div>

  </div>
</template>

<script>
import jQuery from 'jquery'

export default {
  name: 'Sites',
  data: function () {
    return {
      sites: []
    }
  },
  created: function () {
    this.fetchData()
  },
  watch: {
    '$route': 'fetchData'
  },
  methods: {
    fetchData: function () {
      this.fetch()
    },
    fetch: function () {
      var url = '/api/v1/comics/sites/'
      this.$http.get(url).then(function (response) {
        // set data on vm
        var sites = response.body
        sites.map(function (s) {
          s.url = '#/?' + jQuery.param({site: s.site})
        })
        this.sites = sites
      })
    }
  }
}
</script>
