<template>
  <div id="results">
      <b-row class="text-center">        
        <b-col cols="12">
          <b-input-group>
            <b-input-group-prepend>
              <span class="input-group-text">
                <img class="search-icon" src="../../static/Icon_search_big.png"/>
              </span>
            </b-input-group-prepend>
            <b-form-input id="search-here" 
                          class="LoginInput" 
                          size="lg" 
                          placeholder="Buscar Tweets"></b-form-input>
            <b-input-group-append>
            <b-button size="sm" text="Button" @click="searchTwittes(null)" variant="primary">
                <b-spinner small :type="spinner" ></b-spinner>
            Buscar</b-button>
            </b-input-group-append>
          </b-input-group>
        </b-col>
      </b-row>

       <b-row class="text-center">        
        <b-col cols="12">
          <b-alert
      :show="dismissCountDown"
      dismissible
      fade
      variant="warning"
      @dismiss-count-down="countDownChanged"
    >
      Não foram encontrados resultados na pequisa! 
    </b-alert>
            </b-col>
      </b-row>
    <br/>
      <b-list-group>
        <div v-for="item in twittes">
        <b-list-group-item id="list-group" >
        <b-row>
          <b-col cols="2">
            <b-link id="i-link" :href="'https://twitter.com/'+item.screen_name" target="_blank">
              <b-img id="p_image" :src="item.image_url" ledt="true" height="40" width="40" v-bind="mainProps" rounded="circle" alt="Circle image"></b-img>
            </b-link>
          </b-col>
          <b-col cols="8">
          <div >
            <b-row>
              <h5 class="mb-1">{{item.screen_name}}</h5>
              </b-row>
              <b-row>
            <b-link id="t-link" :href="'https://twitter.com/'+item.screen_name+'/status/'+item.id" target="_blank">
            <p class="mb-1">
              {{item.text}}
            </p>
            </b-link>
            </b-row>
          </div>
          </b-col>
          </b-row>  
        </b-list-group-item>
        <hr/>
        </div>
    </b-list-group>
  </div>
</template>
<script>

import { mdbInput } from 'mdbvue';
import { fetchTrendingTopics, fetchTwettsSearch } from '.././services/http'
export default {
  name: 'Search',
  componens: {
      mdbInput
  },
  data() {
    return {
        mainProps: { width: 500, height: 400, class: 'm1' },
        twittes:null,
        topics:null,
        spinner:'none',
        searchTerm:null,
        dismissSecs: 5,
        dismissCountDown: 0,
        showDismissibleAlert: false
      }
  },
  mounted: function() {
    let input = document.getElementById("search-here");
    let that = this;
    input.addEventListener("keyup", function(event) {
      if (event.keyCode === 13) {
        that.searchTwittes(input.value);
      }
  });
  },
  methods: {
    searchTwittes: function(searchTerm) {
      let that = this;
      that.changeSpinner();
      let query = document.getElementById('search-here').value || 'brasil'
      query = searchTerm || query
      fetchTwettsSearch(query).then(res => {
        this.twittes = res.data.twittes
        console.log(this.twittes.length);
        if(this.twittes.length == 0){
          that.noSearchResult(searchTerm);
        }
        that.changeSpinner();
        if(!searchTerm){
          this.$emit('newSearch', query)
        }
      }).catch(function(err){
        that.changeSpinner();
        console.error(err);
      })
    },
    changeSpinner: function(){
      this.spinner = this.spinner == 'grow' ? 'none' : 'grow';    
    },
    noSearchResult:function(term){
      this.searchTerm = term
      this.showAlert();
    },
    countDownChanged(dismissCountDown) {
        this.dismissCountDown = dismissCountDown
    },
    showAlert() {
        this.dismissCountDown = this.dismissSecs
    }
  }
}
</script>
<style>
.UniqueFullWidth .input-group-text {
  width: 48px;
  border-right: none;
  background-color: #FBFBFB;
}

.UniqueFullWidth [class^="fa-"], [class*=" fa-"] {
  display: inline-block;
  width: 100%;
}
.UniqueFullWidth .LoginInput {
  border-left: none;
}

#list-group {
  background-color: #FBFBFB;
  border: none;
}

.input-group {
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
    /* margin:5px auto 0 5px; */
    color: #5E9FCA;
}
</style>
