<template>
  <div>
    <ul>
      <li v-for="data in datalist" :key="data.filmId">
        {{ data.name }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      datalist: [],
    };
  },
  mounted() {
    // console.log("mounted");
    // fetch("/movie.json")
    //   .then((res) => res.json())
    //   .then((res) => {
    //     console.log(res.data.films);
    //     this.datalist = res.data.films;
    //   });
    axios.get("/movie.json").then((res) => {
      console.log(res.data.data.films);
      this.datalist = res.data.data.films;
    });
  },
};
</script>

<style lang="scss" scoped>
$width: 300px;
ul {
  li {
    background: yellow;
    width: $width;
  }
}
</style>
