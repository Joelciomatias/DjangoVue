<template>
  <div id="results">
    <!-- <mdbInput label="Username" icon="user" /> -->
      <b-row class="text-center">        
        <b-col cols="12">
          <b-input-group>
            <b-input-group-prepend>
              <span class="input-group-text">
                <img class="search-icon" src="../../static/Icon_search_big.png"/>
              </span>
            </b-input-group-prepend>
            <b-form-input @keyup="searchTwittes(null)" 
                          id="search-here" 
                          class="LoginInput" 
                          size="lg" 
                          placeholder="Buscar Tweets"></b-form-input>
          </b-input-group>
        </b-col>
      </b-row>
    <br/>
      <b-list-group>
        <div v-for="item in twittes">
        <b-list-group-item 
        active class="flex-column align-items-start">
          <div class="d-flex w-100 justify-content-between">
            <b-link id="i-link" :href="'https://twitter.com/'+item.screen_name" target="_blank">
              <b-img id="p_image" :src="item.image_url" ledt="true" height="40" width="40" v-bind="mainProps" rounded="circle" alt="Circle image"></b-img>
            </b-link>
            <h5 class="mb-1">{{item.screen_name}}</h5>
            <small>{{item.name}}</small>
          </div>
          <b-link id="t-link" :href="'https://twitter.com/'+item.screen_name+'/status/'+item.id" target="_blank">
          <p class="mb-1">
            {{item.text}}
          </p>
          </b-link>
          <!-- <small></small> -->
        </b-list-group-item>
        <hr/>
        </div>
    </b-list-group>
  </div>
</template>
<script>

import { mdbInput } from 'mdbvue';
import { fetchTrendingTopics, fetchTwettsSearch } from '.././services/http'
// import func from '../vue-temp/vue-editor-bridge';
export default {
  name: 'Search',
  componens: {
      mdbInput
  },
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
    searchTwittes: function(searchTerm) {
      let query = document.getElementById('search-here').value || 'brasil'
      fetchTwettsSearch(query).then(res => {
        this.twittes = res.data.twittes
        console.log(res.data.twittes);
      })
    },
  }
}
</script>
<style>
.UniqueFullWidth .input-group-text {
  width: 48px;
  border-right: none;
  background-color: #ffffff;
}
.UniqueFullWidth [class^="fa-"], [class*=" fa-"] {
  display: inline-block;
  width: 100%;
}
.UniqueFullWidth .LoginInput {
  border-left: none;
}
.input-group {
  /* max-width: 500px; */
  padding:2% 5%;
}
.search-icon{
  height: 30px;
  width: 30px;
}
#t-link {
  text-decoration: none;
  color: inherit;
}
#p_image {
  margin-left: -5px;
}
h5 {
    margin:5px auto 0 5px;
}
</style>
