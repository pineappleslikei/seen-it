<template>
  <div class="aResult" @click="showModal">
    <div>
      <img class="poster-frame" :src="posterPath" @error="replaceImage" />
    </div>
    <div class="search-text">
      <h1>{{ movieName }}</h1>
    </div>
  </div>
  <ResultModal
    v-show="isModalVisible"
    :movie-id="movieId"
    @close="closeModal"
  />
</template>

<script>
import ResultModal from "./ResultModal.vue";

export default {
  name: "SearchResult",
  data() {
    return {
      isModalVisible: false,
    };
  },
  components: {
    ResultModal,
  },
  props: {
    movieName: String,
    movieId: Number,
    moviePic: String,
  },
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
    showModal() {
      this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
    },
  },
};
</script>

<style>
.search-text {
  width: 75em;
}
.poster-frame {
  width: 100px;
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
