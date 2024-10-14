<template>
  <div class="header">
    <i class="iconfont icon-bangzhu" @click="handleBack"></i>
    <slot></slot>
  </div>
</template>

<script>
export default {
  methods: {
    handleBack() {
      this.$router.back();
    },
  },
};
</script>

<style lang="scss" scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 2.75rem;
  line-height: 2.75rem;
  background-color: white;
  text-align: center;

  i {
    font-size: 30px;
    position: fixed;
    left: 0.625rem;
    top: 0;
    height: 2.75rem;
    line-height: 2.75rem;
  }
}
</style>
