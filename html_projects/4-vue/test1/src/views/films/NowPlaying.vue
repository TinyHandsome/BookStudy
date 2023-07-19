<template>
  <div>
    <ul>
      <li
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
      </li>
    </ul>
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
    });
  },
  methods: {
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
ul {
  li {
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
