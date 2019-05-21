<template>
  <div id="home">
    <b-row class="text-center">
      <b-col></b-col>
      <b-col cols="8">
        <img id="logo" src="../../static/Twitter_logo_blue.png" width='' height=''  alt="Fluid-grow image"/>
      </b-col>
      <b-col></b-col>
    </b-row>
    <div id=container>
      <b-row >
        <b-col class="text-left">
          <ul class="home-list">
          <h4 class="text-left">Trending Now</h4>
            <div v-for="item in topics">
              <b-link :href="item.url" target="_blank">
                <li>{{ item.name }}</li>
              </b-link>
            </div>
          </ul>
        </b-col>
        <b-col class="text-left">
          <ul class="home-list">
            <h4>Recent Searches</h4>
            <div v-for="item in searches">
            <b-link href="" @click="researchTerm(item)">
                <li>{{ item }}</li>
              </b-link>
            </div>
          </ul>
        </b-col>
      </b-row>
      <br/>
      <search @newSearch="updateSearchs" ref="child"></search>
    </div>
  </div>
</template>
<script>
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
        topics:null,
        searches:[],
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
      })
    },
    updateSearchs: function(value){
      this.searches.push(value);
      if(this.searches.length > 5){
        this.searches.shift()
      }
    },
    researchTerm: function(item){
      this.$refs.child.searchTwittes(item)
    }
  }
}
</script>
<style>
#home {
  background-color: #FBFBFB;
  padding: 50px 15px 15px 15px;
  min-height: 50rem;
}
#container {
  padding-top: 20px;
}
#logo {

}
h4 {
  color: #5E9FCA;
}
#example-2{
  color:#F5F5F5;
}
ul li {
  list-style-type: none;
  color: #5E9FCA;
}
/* blue #5E9FCA */
</style>
