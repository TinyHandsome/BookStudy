<template>
    <div>
        <div class="swiper">
            <div class="swiper-wrapper">
                <div
                    v-lt="{ index, length: datalist.length }"
                    class="swiper-slide"
                    v-for="(data, index) in datalist"
                    :key="data"
                >
                    {{ data }}
                </div>
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
    data() {
        return {
            datalist: [],
        };
    },
    mounted() {
        setTimeout(() => {
            this.datalist = ["aa", "bb", "cc"];
        }, 2000);
    },
    directives: {
        lt: {
            mounted(el, binding) {
                console.log("插进来啦");
                let { index, length } = binding.value;
                if (index === length - 1) {
                    console.log("最后一个节点");
                    var mySwiper = new Swiper(".swiper", {
                        modules: [Pagination],
                        // 循环模式选项
                        loop: true,

                        // 如果需要分页器
                        pagination: {
                            el: ".swiper-pagination",
                        },
                        on: {
                            slideChange() {
                                console.log("便咯" + this.activeIndex);
                            },
                        },
                    });
                }
            },
        },
    },
};
</script>

<style scoped>
.swiper {
    width: 600px;
    height: 300px;
}
</style>
