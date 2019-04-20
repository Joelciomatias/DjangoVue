<template>
  <div id="app">
    <ul id="example-1">
      <div v-for="item in topics">
        <a :href="item.url" target="_blank">
          <li>{{ item.name }}</li>
        </a>
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
          <!-- </a> -->
      </div>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  name: 'App',
  data() {
    return {
      items: [
        { message: 'Algo' },
        { message: 'Outro' }
      ],
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
