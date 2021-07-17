<template>
  <div>
    <div class="details-header">
      <img :src="poster" alt="" />
      <h1>{{ title }}</h1>
      <p>
        <em>{{ genre }}</em
        >, released {{ releaseDate }}
      </p>
    </div>
    <div class="details-body">
      <p>{{ synopsis }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieDetail",
  props: ["title", "genre", "synopsis", "releaseDate", "poster"],
};
</script>
