<template>
  <div>
    <div id="search-container">
      <input
        v-model.trim="search_term"
        @keyup.enter="getResults"
        placeholder="Search"
      />
      <button @click="getResults">Search</button>
    </div>
    <div id="result-container">
      <div v-for="movie in movies" :key="movie">
        <SearchResult
          :movie-name="movie.title"
          :movie-description="movie.overview"
          :movie-pic="movie.poster_path"
        />
      </div>
    </div>
  </div>
</template>

<script>
import SearchResult from "../components/SearchResult.vue";
import axios from "axios";

const backPath = "http://127.0.0.1:5000/";

export default {
  name: "Search",
  components: {
    SearchResult,
  },
  data() {
    return {
      movies: {},
      search_term: "",
    };
  },
  methods: {
    getResults() {
      var path = backPath + this.search_term;
      axios.get(path).then((response) => {
        this.movies = response.data;
      });
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
body {
  margin: 0px;
}
#result-container {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}
#search-container {
  padding: 10px 0px 10px 0px;
}
</style>
