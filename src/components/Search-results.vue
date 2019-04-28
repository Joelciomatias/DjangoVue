<template>
  <div id="results">
    <input type="text" id="search-here">
    <br/>
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
import { fetchTrendingTopics, fetchTwettsSearch } from '.././services/http'
// import func from '../vue-temp/vue-editor-bridge';
export default {
  name: 'Search',
  data() {
    return {
        mainProps: { width: 500, height: 400, class: 'm1' },
        twittes:null,
        topics:null
      }
  },
  mounted: function() {
  },
  methods: {
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
