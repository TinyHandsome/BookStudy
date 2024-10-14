<template>
    <div>
        <div class="swiper">
            <div class="swiper-wrapper">
                <slot></slot>
            </div>
            <div class="swiper-pagination"></div>
        </div>
    </div>
</template>

<script>
import Swiper from "swiper";
import "swiper/css";
import "swiper/css/pagination";
import { Pagination } from "swiper/modules";

export default {
    props:{
        loop: {
            type: Boolean,
            default: true
        },
        slidesPerView: {
            type: Number,
            default: 1
        },
        spaceBetween: {
            type: Number,
            default: 0
        }
    },
    mounted() {
        var mySwiper = new Swiper(".swiper", {
            modules: [Pagination],
            // 循环模式选项
            loop: this.loop,
            slidesPerView: this.slidesPerView,
            spaceBetween: this.spaceBetween,

            // 如果需要分页器
            pagination: {
                el: ".swiper-pagination",
            },
            on: {
                slideChange:() => {
                    console.log("便咯" + mySwiper.activeIndex);
                    this.$emit("kerwinSlideChange", mySwiper.activeIndex)
                },
            },
        });
    },
};
</script>

<style scoped>
.swiper {
    width: 600px;
    height: 300px;
}
</style>
