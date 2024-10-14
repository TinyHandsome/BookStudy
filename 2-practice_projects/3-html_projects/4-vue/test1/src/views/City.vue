<template>
  <div class="city">
    <van-index-bar :index-list="computedList" @select="handleChange">
      <div v-for="data in cityList" :key="data.type">
        <van-index-anchor :index="data.type" />
        <van-cell
          :title="item.name"
          v-for="item in data.list"
          :key="item.cityId"
          @click="handleClick(item)"
        />
      </div>
    </van-index-bar>
  </div>
</template>

<script>
import http from "@/util/http";
import { Toast } from "vant";
import obj from "@/util/mixinObj";

export default {
  mixins: [obj],
  data() {
    return {
      cityList: [],
    };
  },
  computed: {
    computedList() {
      return this.cityList.map((item) => item.type);
    },
  },
  mounted() {
    http({
      url: "/gateway?k=1480767",
      headers: {
        "X-Host": "mall.film-ticket.city.list",
      },
    }).then((res) => {
      //   console.log(res.data.data.cities);
      this.cityList = this.renderCity(res.data.data.cities);
      // 316条 ==> a、b进行分组
      // 利用转化后的数组，结合组件库进行渲染页面
    });
  },
  methods: {
    handleChange(e) {
      // console.log("change", e);
      Toast(e);
    },
    renderCity(list) {
      console.log(list);
      var cityList = [];

      var letterList = [];
      for (var i = 65; i < 91; i++) {
        letterList.push(String.fromCharCode(i));
      }
      letterList.forEach((letter) => {
        var newList = list.filter(
          (item) => item.pinyin.substring(0, 1).toUpperCase() === letter
        );

        newList.length > 0 &&
          cityList.push({
            type: letter,
            list: newList,
          });
      });
      console.log(cityList);
      return cityList;
    },
    handleClick(item) {
      // console.log(item);
      // this.$store.state.cityName = item.name;

      this.$store.commit("changeCityName", item.name);
      this.$store.commit("changeCityId", item.cityId);
      this.$router.back();
    },
  },
};
</script>

<style lang="scss">
.van-toast--html,
.van-toast--text {
  min-width: 30px;
}
</style>
