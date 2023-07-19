<template>
  <div>
    <film-swiper :key="datalist.length">
      <!-- <div class="swiper-slide">111</div>
      <div class="swiper-slide">222</div>
      <div class="swiper-slide">333</div> -->
      <!-- <film-swiper-item>111</film-swiper-item>
      <film-swiper-item>222</film-swiper-item>
      <film-swiper-item>333</film-swiper-item> -->
      <film-swiper-item
        class="filmswiperitem"
        v-for="data in datalist"
        :key="data.id"
      >
        <img :src="data.imgUrl" />
      </film-swiper-item>
    </film-swiper>
    <film-header class="sticky"></film-header>
    <!-- <div>二级的声明式导航</div> -->
    <router-view></router-view>
  </div>
</template>

<script>
import filmSwiper from "@/components/films/FilmSwiper";
import filmSwiperItem from "@/components/films/FilmSwiperItem";
import filmHeader from "@/components/films/FilmHeader";

import axios from "axios";
export default {
  data() {
    return {
      datalist: [],
    };
  },
  mounted() {
    // setTimeout(() => {
    // this.datalist = ["111", "bbb", "ccc"];
    // }, 1000);
    axios.get("/banner.json").then((res) => {
      console.log(res.data);
      this.datalist = res.data.banner;
    });
  },
  components: {
    filmSwiper,
    filmSwiperItem,
    filmHeader,
  },
};
</script>
<style lang="scss" scoped>
.filmswiperitem {
  img {
    width: 100%;
  }
}
.sticky {
  position: sticky;
  top: 0px;
  background: white;
}
</style>
