<template>
    <div>
        <MySwiper v-if="items.length" :slidesPerView="3" :loop="false" @kerwinSlideChange="handleChange">
            <MySwiperItem v-for="item in items" :key="item">
                {{ item }}
            </MySwiperItem>
        </MySwiper>
    </div>
</template>

<script>
import MySwiper from "./MySwiper.vue";
import MySwiperItem from "./MySwiperItem.vue";
export default {
    components: {
        MySwiper,
        MySwiperItem,
    },
    data() {
        return { 
            items: [],
        };
    },
    mounted() {
        setTimeout(() => {
            this.items = ["aaa", "bbb", "ccc", "ddd", "eee"];
        }, 2000);
    },
    methods: {
        handleChange(index){
            console.log("asdf-", index);
        }
    }
};
</script>

<style scoped></style>
