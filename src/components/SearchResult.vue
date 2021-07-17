<template>
  <div class="aResult">
    <div>
      <img class="poster-frame" :src="posterPath" @error="replaceImage" />
    </div>
    <div class="search-text">
      <h1>{{ movieName }}</h1>
      <p>{{ movieDescription }}</p>
    </div>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: "SearchResult",
  props: {
    movieName: String,
    movieDescription: String,
    moviePic: String,
  },
  // how do we do async in js?
  computed: {
    posterPath: function () {
      var path = this.moviePic;
      var pic_url = "https://image.tmdb.org/t/p/original/";
      return pic_url + path;
    },
  },
  methods: {
    replaceImage: function (e) {
      e.target.src = require("../assets/default.jpg");
    },
  },
};
</script>

<style>
.search-text {
  width: 75em;
}
.poster-frame {
  width: 200px;
  margin: 10px;
}
.aResult {
  display: flex;
  transition: 0.2s;
}
.aResult:hover {
  transform: scale(1.02);
  background-color: gainsboro;
  border: 1px solid black;
  transition: 0.2s;
}
p,
h1 {
  text-align: left;
}
</style>
