<template>
  <div class="swiper-container kerwin">
    <div class="swiper-wrapper">
      <slot></slot>
    </div>
    <div class="swiper-pagination"></div>
  </div>
</template>

<script>
import Swiper from "swiper/bundle";
import "swiper/swiper-bundle.css";
export default {
  props: {
    loop: {
      type: Boolean,
      default: true,
    },
  },
  mounted() {
    new Swiper(".kerwin", {
      pagination: {
        el: ".swiper-pagination",
      },
      loop: this.loop,
      autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      },
    });
  },
};
</script>
