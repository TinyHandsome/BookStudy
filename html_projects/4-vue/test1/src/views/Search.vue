<template>
  <div>
    <form action="/">
      <van-search
        v-model="value"
        show-action
        placeholder="请输入搜索关键词"
        @search="onSearch"
        @cancel="onCancel"
      />
    </form>
    <ul v-if="value">
      <li v-for="data in computedList" :key="data.cinemaId">
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
</template>

<script>
export default {
  data() {
    return {
      value: "",
    };
  },
  methods: {
    onSearch() {},
    onCancel() {
      this.$router.back();
    },
  },
  computed: {
    computedList() {
      return this.$store.state.cinemaList.filter(
        (item) =>
          item.name.toUpperCase().includes(this.value.toUpperCase()) ||
          item.address.toUpperCase().includes(this.value.toUpperCase())
      );
    },
  },
  mounted() {
    if (this.$store.state.cinemaList.length === 0) {
      this.$store.dispatch("getCinemaData", this.$store.state.cityId);
    } else {
    }
  },
};
</script>
<style lang="scss" scoped>
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
