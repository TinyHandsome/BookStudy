<template>
  <div>
    <van-nav-bar
      title="影院"
      ref="navbar"
      @click-left="handleLeft"
      @click-right="handleRight"
    >
      <template #left
        >{{ cityName }}<van-icon name="arrow-down"></van-icon>
      </template>
      <template #right>
        <van-icon name="search" size="20" color="black" />
      </template>
    </van-nav-bar>

    <div class="box" :style="{ height: height }">
      <ul>
        <li v-for="data in $store.state.cinemaList" :key="data.cinemaId">
          <div class="left">
            <div class="cinema_name">{{ data.name }}</div>
            <div class="cinema_text">{{ data.address }}</div>
          </div>
          <div class="right cinema_name">
            <div style="color: red">￥{{ data.lowPrice / 100 }}起</div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
import BetterScroll from "better-scroll";
import { mapState, mapActions, mapMutations } from "vuex";

export default {
  data() {
    return {
      // cinemaList: [],
      height: "50px",
    };
  },
  computed: {
    ...mapState(["cinemaList", "cityId", "cityName"]),
  },
  mounted() {
    // 动态计算高度
    this.height =
      document.documentElement.clientHeight -
      document.querySelector("footer").offsetHeight -
      this.$refs.navbar.$el.offsetHeight +
      "px";

    // dispatch: 分发
    if (
      // this.$store.state.cinemaList.length === 0
      this.cinemaList.length === 0
    ) {
      this.getCinemaData(this.cityId).then((res) => {
        this.$nextTick(() => {
          new BetterScroll(".box", {
            scrollbar: {
              fade: true,
            },
          });
        });
      });
    } else {
      new BetterScroll(".box", {
        scrollbar: {
          fade: true,
        },
      });
    }

    // http({
    //   url: `/gateway?cityId=${this.$store.state.cityId}&ticketFlag=1&k=4312294`,
    //   headers: {
    //     "X-Host": "mall.film-ticket.cinema.list",
    //   },
    // }).then((res) => {
    //   console.log(res.data.data.cinemas);
    //   this.cinemaList = res.data.data.cinemas;

    //   this.$nextTick(() => {
    //     new BetterScroll(".box", {
    //       scrollbar: {
    //         fade: true,
    //       },
    //     });
    //   });
    // });
  },
  methods: {
    ...mapActions(["getCinemaData"]),
    ...mapMutations(["clearCinema"]),
    handleLeft() {
      // console.log("left");
      this.$router.push("/city");
      // 清空cinemaList
      this.clearCinema();
    },
    handleRight() {
      this.$router.push("/cinemas/search");
    },
  },
};
</script>
<style lang="scss" scoped>
.box {
  // height: 38.625rem;
  overflow: hidden;

  // 修正滚动条的位置
  position: relative;
}
li {
  padding: 0.9375rem;
  display: flex;
  justify-content: space-between;

  .left {
    width: 13.25rem;
  }

  .cinema_name {
    font-size: 15px;
  }

  .cinema_text {
    color: #797d82;
    font-size: 12px;
    margin-top: 5px;

    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
}
</style>
