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
    this.getTrendingTopics();
  },
  methods: {
      getTrendingTopics: function() {
        var app = this;
        var topics = null;
        axios.get(process.env.API_URL + "/api_example/topics/23424768/").then(response => {
          topics = response.data.topics
            topics = topics.slice(0,5)
            console.log(topics);
            this.topics = topics
        }).catch((err) => {
            console.error(err);
            alert(`Houve um erro ao carregar dados(${err.status.code}): `)
        });
      },
      searchTwittes: function() {
        var app = this;
        var query = document.getElementById('search-here').value || 'brasil'
        axios.get(process.env.API_URL + `/api_example/search/${query}/`).then(response => {
            console.log(response.data.twittes);
            this.twittes = response.data.twittes
        });
      },
  }
}
</script>
<style>
</style>
