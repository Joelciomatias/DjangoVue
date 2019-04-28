<template>
  <div id="searchs">
     <ul id="example-1">
        <div v-for="item in topics2">
            <b-link :href="item.url" target="_blank">
            <li>{{ item.name }}</li>
            </b-link>
        </div>
        </ul>
  </div>
</template>
<script>

import { fetchTrendingTopics, fetchTwettsSearch } from '.././services/http'

export default {
    name: 'Homelist',

data() {
    return {
        searchs:null,
        topics:null
    }
  },
  mounted: function() {
  },
  methods: {
      
}
}
</script>
<style>
</style>
