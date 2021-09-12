<template>
  <div class="modal-backdrop">
    <div class="modal">
      <img class="poster-frame" :src="posterPath" @error="replaceImage" />
      <h1>{{ movieName }}</h1>
      <p>{{ movieDescription }}</p>
      <div id="button-container">
        <button class="btn btn-confirm">Add to my movies</button>
        <button class="btn btn-decline" @click="close">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Modal",
  methods: {
    close() {
      this.$emit("close");
    },
  },
  props: {
    movieId: Number,
  },
};
</script>

<style>
.modal-backdrop {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background: #ffffff;
  box-shadow: 2px 2px 20px 1px;
  overflow-x: auto;
  display: flex;
  flex-direction: column;
  border-radius: 8px;
  padding: 10px;
}
.btn {
  border-radius: 8px;
  border: none;
  color: whitesmoke;
  font-weight: bold;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  padding: 5px;
}

.btn-confirm {
  background-color: rgb(43, 171, 29);
}

.btn-decline {
  background-color: rgb(255, 68, 40);
}
</style>
