

var vue = new Vue({
  el: '#app',
  data: {
    message: 'Comkc',
    comics: [],
    page: 1
  },
  ready: function() {
    this.fetch();
  },
  methods: {
    'fetch': function() {
      var url = '/api/v1/comics/?per_page=8&page=' + this.page;
      if (/[\?&]random$/.test(location.href)) {
        url += '&random'
      }
      this.$http.get(url).then(function (response) {
        // set data on vm
      this.$set('comics', response.data);
      })
    },
    'prePageEvent': function() {
      if (this.page < 2) {return}
      this.page --;
      this.fetch();
    },
    'nextPageEvent': function() {
      this.page ++;
      this.fetch();
    }
  }
})
