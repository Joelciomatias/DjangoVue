<template>
  <div id="app">
    <img src="../static/Twitter_logo_blue.png" width='' height=''  alt="Fluid-grow image"/>

    <ul id="example-1">
      <div v-for="item in topics">
        <b-link :href="item.url" target="_blank">
          <li>{{ item.name }}</li>
        </b-link>
      </div>
    </ul>
    <br/>
    
    <input type="text" id="search-here">
    <button @click="searchTwittes()">Search twittes</button>
      <div v-for="item in twittes">
            <img :alt="item.screen_name" :src="item.image_url"/>
            <li>{{ item.screen_name +' - '+item.name}}</li>
            <p>{{item.text}}</p>
            <hr/>
      </div>
  </div>
  
</template>
<script>
import axios from 'axios';
import { fetchTrendingTopics, fetchTwettsSearch } from './services/http'
// import func from '../vue-temp/vue-editor-bridge';
export default {
  name: 'App',
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
    searchTwittes: function() {
      let query = document.getElementById('search-here').value || 'brasil'
      fetchTwettsSearch(query).then(res => {
        this.twittes = res.data.twittes
        // console.log(res.data.twittes);
      })
    },
  }
}
</script>
<style>
</style>
