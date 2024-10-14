<template>
  <div>
    <van-list
      v-model="loading"
      :finished="finished"
      finished-text="我是有底线的"
      @load="onLoad"
      :immediate-check="false"
    >
      <!-- <van-cell v-for="item in list" :key="item" :title="item" /> -->

      <van-cell
        v-for="data in datalist"
        :key="data.filmId"
        @click="handleChangePage(data.filmId)"
      >
        <img :src="data.poster" alt="" />
        <div>
          <div class="title">{{ data.name }}</div>
          <div class="content">
            <div :class="data.grade ? '' : 'hidden'">
              观众评分：<span style="color: red">{{ data.grade }}</span>
            </div>
            <div class="actors">主演：{{ data.actors | actorsFilter }}</div>
            <div>{{ data.nation }} | {{ data.runtime }}分钟</div>
          </div>
        </div>
        <!-- <router-link to="/detail">{{ data }}</router-link> -->
      </van-cell>
    </van-list>
  </div>
</template>

<script>
import axios from "axios";
import Vue from "vue";
import http from "@/util/http";

Vue.filter("actorsFilter", (data) => {
  // console.log(data.map((item) => item.name));

  if (data === undefined) return "暂无主演";
  return data.map((item) => item.name).join(" ");
});
export default {
  data() {
    return {
      datalist: [],
      loading: false,
      finished: false,
      current: 1,
      total: 0,
    };
  },
  mounted() {
    // axios({
    //   url: "https://m.maizuo.com/gateway?cityId=440300&pageNum=1&pageSize=10&type=1&k=3602463",
    //   headers: {
    //     "X-Client-Info":
    //       '{"a":"3000","ch":"1002","v":"5.2.1","e":"1689149181904756335738881"}',
    //     "X-Host": "mall.film-ticket.film.list",
    //   },
    // })
    http({
      url: "/gateway?cityId=440300&pageNum=1&pageSize=10&type=1&k=3602463",
      headers: {
        "X-Host": "mall.film-ticket.film.list",
      },
    }).then((res) => {
      console.log(res.data.data.films);
      this.datalist = res.data.data.films;
      this.total = res.data.data.total;
    });
  },
  methods: {
    onLoad() {
      // 总长度匹配，禁用懒加载功能
      if (this.datalist.length === this.total && this.total != 0) {
        this.finished = true;
        return;
      }
      console.log("到底了");
      this.current++;

      http({
        url: `/gateway?cityId=${this.$store.state.cityId}&pageNum=${this.current}&pageSize=10&type=1&k=3602463`,
        headers: {
          "X-Host": "mall.film-ticket.film.list",
        },
      }).then((res) => {
        // console.log(res.dat  wa.data.films);
        this.datalist = [...this.datalist, ...res.data.data.films];
      });
      this.loading = false;
    },
    handleChangePage(id) {
      console.log(id);
      // 编程式导航
      // location.href = "#/detail";
      // 通过路径跳转
      // this.$router.push(`/detail/${id}`);

      // 通过命名路由跳转
      this.$router.push({
        name: "detail",
        params: {
          myid: id,
        },
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.van-list {
  .van-cell {
    overflow: hidden;
    padding: 0.9375rem;

    img {
      width: 4.125rem;
      float: left;
    }

    .title {
      font-size: 16px;
    }

    .content {
      font-size: 13px;
      color: gray;

      .actors {
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        width: 12.5rem;
      }
    }
  }
}

.hidden {
  visibility: hidden;
}
</style>
