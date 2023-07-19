<template>
  <div v-if="filmInfo">
    <!-- <img :src="filmInfo.poster" alt="" /> -->
    <div
      :style="{
        backgroundImage: 'url(' + filmInfo.poster + ')',
      }"
      class="poster"
    ></div>
    <div class="content">
      <div>{{ filmInfo.name }}</div>
      <div>
        <div class="content-bottom">{{ filmInfo.category }}</div>
        <div class="content-bottom">{{ filmInfo.premiereAt * 1000 }}上映</div>
        <div class="content-bottom">
          {{ filmInfo.nation }} | {{ filmInfo.runtime }}分钟
        </div>
        <div class="content-bottom"></div>
        <div class="content-bottom"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import http from "@/util/http";

export default {
  data() {
    return {
      filmInfo: null,
    };
  },
  created() {
    // console.log("created", location.href);
    console.log("created", this.$route.params.myid);
    // axios 利用id发请求到详情接口，获取详细拿数据，布局页面
    // axios({
    //   url: `https://m.maizuo.com/gateway?filmId=${this.$route.params.myid}&k=2382781`,
    //   headers: {
    //     "X-Client-Info":
    //       '{"a":"3000","ch":"1002","v":"5.2.1","e":"1689149181904756335738881","bc":"310100"}',
    //     "X-Host": "mall.film-ticket.film.info",
    //   },
    // })

    http({
      url: `/gateway?filmId=${this.$route.params.myid}&k=2103749`,
      headers: {
        "X-Host": "mall.film-ticket.film.info",
      },
    }).then((res) => {
      console.log(res.data);
      this.filmInfo = res.data.data.film;
    });
  },
};
</script>

<style lang="scss" scoped>
.poster {
  width: 100%;
  height: 13.125rem;
  background-position: center;
  background-size: cover;
}

.content {
  padding: 0.9375rem;
  font-size: 18px;
  .content-bottom {
    color: #797d82;
    font-size: 12px;
    margin-top: 0.25rem;
  }
}
</style>
