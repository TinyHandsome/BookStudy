<template>
  <div class="swiper-container kerwin">
    <div class="swiper-wrapper">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import Swiper from "swiper/bundle";
import "swiper/swiper-bundle.css";
export default {
  props: {
    perview: {
      type: Number,
      default: 1,
    },
  },
  mounted() {
    new Swiper(".kerwin", {
      slidesPerView: this.perview,
      spaceBetween: 30,
      freeMode: true,
    });
  },
};
</script>
