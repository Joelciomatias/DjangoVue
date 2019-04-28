<template>
  <div id="results">
    <!-- <input type="text" id="search-here"> -->
    <!-- <mdbInput label="Username" icon="user" /> -->
    <b-input-group>
      <b-input-group-prepend>
        <span class="input-group-text"><i src="../../static/Icon_search_big.png" 
        class="fa fa-search fa-lg"></i></span>
      </b-input-group-prepend>
      <b-form-input id="search-here" class="LoginInput" size="lg" placeholder="Buscar Tweets">
      </b-form-input>
        <b-input-group-append>
          <b-button @click="searchTwittes()" variant="info"><i class="fa fa-arrow-right"  aria-hidden="true"></i></b-button>
        </b-input-group-append>
    </b-input-group>
    <br/>
      <div v-for="item in twittes">
            <img :alt="item.screen_name" :src="item.image_url"/>
            <li>{{ item.screen_name +' - '+item.name}}</li>
            <p>{{item.text}}</p>
            <hr/>
      </div>
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
    searchTwittes: function() {
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

</style>
