export default {
  methods: {
    prePage: function () {
      var page = this.currentPage() - 1
      if (page < 2) {
        page = 1
      }
      return page
    },
    nextPage: function () {
      var page = this.currentPage() + 1
      return page
    },
    currentPage: function () {
      return parseInt(this.$route.query.page) || 1
    }
  }
}
