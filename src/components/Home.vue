<template>
  <div id="home">
    <img src="../../static/Twitter_logo_blue.png" width='' height=''  alt="Fluid-grow image"/>
    <ul id="example-1">
      <div v-for="item in topics">
        <b-link :href="item.url" target="_blank">
          <li>{{ item.name }}</li>
        </b-link>
      </div>
    </ul>
    <br/>
    <search></search>
  </div>
</template>
<script>
import axios from 'axios';
import Search from './Search-results.vue'
import { fetchTrendingTopics, fetchTwettsSearch } from '.././services/http'
// import func from '../vue-temp/vue-editor-bridge';
export default {
  name: 'App',
  components:{
    'search':Search
  },
  data() {
    return {
        mainProps: { width: 500, height: 400, class: 'm1' },
        twittes:null,
        topics:null
      }
  },
  mounted: function() {
    this.getTrendingTopics()
    },
    methods: {
    getTrendingTopics: function() {
      let regionId = 23424768
      fetchTrendingTopics(regionId).then(res => {
        this.topics = res.data.topics.slice(0,5)
        // console.log(this.topics);
      })
    },
  }
}
</script>
<style>
</style>
