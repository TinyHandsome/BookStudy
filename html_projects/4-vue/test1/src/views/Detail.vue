<template>
  <div v-if="filmInfo">
    <detail-header v-scroll="50">
      {{ filmInfo.name }}
    </detail-header>
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
        <div class="content-bottom">
          {{ filmInfo.premiereAt | dataFilter }}上映
        </div>
        <div class="content-bottom">
          {{ filmInfo.nation }} | {{ filmInfo.runtime }}分钟
        </div>
        <div
          class="content-bottom"
          style="line-height: 15px"
          :class="isHidden ? 'hidden' : ''"
        >
          {{ filmInfo.synopsis }}
        </div>
        <div style="text-align: center">
          <i
            class="iconfont"
            :class="isHidden ? 'icon-caidan' : 'icon-chuangzuo'"
            @click="isHidden = !isHidden"
          ></i>
        </div>
        <div class="content-bottom"></div>
      </div>

      <div>
        <div>演职人员</div>
        <detail-swiper :perview="3.5" name="actors">
          <detail-swiper-item
            v-for="(data, index) in filmInfo.actors"
            :key="index"
          >
            <div
              :style="{
                backgroundImage: 'url(' + data.avatarAddress + ')',
              }"
              class="avatar"
            ></div>
            <div style="text-align: center; font-size: 12px">
              {{ data.name }}
            </div>
            <div style="text-align: center; font-size: 13px; color: grey">
              {{ data.role }}
            </div>
          </detail-swiper-item>
        </detail-swiper>
      </div>

      <div>
        <div>剧照</div>
        <detail-swiper :perview="2" name="photos">
          <detail-swiper-item
            v-for="(data, index) in filmInfo.photos"
            :key="index"
          >
            <div
              :style="{
                backgroundImage: 'url(' + data + ')',
              }"
              class="avatar"
              @click="handlePreview(index)"
            ></div>
          </detail-swiper-item>
        </detail-swiper>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import http from "@/util/http";
import obj from "@/util/mixinObj";
import moment from "moment";
import Vue from "vue";

import detailSwiper from "@/components/detail/DetailSwiper";
import detailSwiperItem from "@/components/detail/DetailSwiperItem";
import detailHeader from "@/components/detail/DetailHeader";
import { ImagePreview } from "vant";
// 设置成中文
moment.locale("zh-cn");

Vue.filter("dataFilter", (date) => {
  return moment(date * 1000).format("YYYY-MM-DD");
});

Vue.directive("scroll", {
  inserted(el, binding) {
    // el是绑定在谁身上，就拿到谁的dom节点
    // console.log(el, binding);
    el.style.display = "none";

    window.onscroll = () => {
      if (
        (document.documentElement.scrollTop || document.body.scrollTop) >
        binding.value
      ) {
        el.style.display = "block";
      } else {
        el.style.display = "none";
      }
    };
  },

  // 销毁执行
  unbind() {
    window.onscroll = null;
  },
});

export default {
  mixins: [obj],
  data() {
    return {
      filmInfo: null,
      isHidden: true,
    };
  },
  components: {
    detailSwiper,
    detailSwiperItem,
    detailHeader,
  },
  methods: {
    handlePreview(index) {
      ImagePreview({
        images: this.filmInfo.photos,
        startPosition: index,
        closeable: true,
        closeIconPosition: "top-left",
      });
    },
  },
  mounted() {
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

  // mounted() {
  //   window.onscroll = () => {
  //     console.log("scroll");

  //     if (document.documentElement.scrollTop > 50) {
  //       console.log("显示");
  //     } else {
  //       console.log("隐藏");
  //     }
  //   };
  // },
  destroyed() {
    window.onscroll = null;
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

.hidden {
  overflow: hidden;
  height: 30px;
}

.avatar {
  width: 100%;
  height: 5.3125rem;
  background-position: center;
  background-size: cover;
}
</style>
