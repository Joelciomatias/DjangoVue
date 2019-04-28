<template>
  <div id="home">
    <b-row class="text-center">
      <b-col></b-col>
      <b-col cols="8">
        <img id="logo" src="../../static/Twitter_logo_blue.png" width='' height=''  alt="Fluid-grow image"/>
      </b-col>
      <b-col></b-col>
    </b-row class="text-center">
    <div id=container>
      <b-row>
        <b-col>
          <h4>Trending Now</h4>
          <ul id="example-1">
            <div v-for="item in topics">
              <b-link :href="item.url" target="_blank">
                <li>{{ item.name }}</li>
              </b-link>
            </div>
          </ul>
        </b-col>
        <b-col>
          <ul id="example-1">
            <div v-for="item in topics2">
              <b-link :href="item.url" target="_blank">
                <li>{{ item.name }}</li>
              </b-link>
            </div>
          </ul>
        </b-col>
      </b-row>
      <br/>
      <b-row class="text-center">
        <b-col cols="12">
          <search></search>
        </b-col>
      </b-row>
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
        topics2:null
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
        this.topics2 = res.data.topics.slice(5,10)
        // console.log(this.topics);
      })
    },
  }
}
</script>
<style>
#home {
  background-color: #F5F5F5;
  padding: 50px 15px 15px 15px;
  min-height: 50rem;
}
#container{
padding-top: 20px;
}
#logo{
  /* margin-left: 40%; */
}
h4 {
  color: #5E9FCA;
}
ul li {
  list-style-type: none;
}
/* blue #5E9FCA */
</style>
