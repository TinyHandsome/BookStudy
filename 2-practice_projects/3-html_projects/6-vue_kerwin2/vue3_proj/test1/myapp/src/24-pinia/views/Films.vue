<template>
    <div>
        <van-swipe class="my-swipe" :autoplay="3000" indicator-color="white">
            <van-swipe-item v-for="(item, index) in datalist" :key="item.id">
                <img :src="item.imgUrl" alt="" style="width: 100%">
            </van-swipe-item>
        </van-swipe>

        <ul class="header">
            <router-link
                to="/films/nowplaying"
                custom
                v-slot="{ isActive, navigate }"
            >
                <li @click="navigate">
                    <span :class="isActive ? 'kerwinactive' : ''"
                        >正在热映</span
                    >
                </li>
            </router-link>
            <router-link
                to="/films/comingsoon"
                custom
                #="{ isActive, navigate }"
            >
                <li @click="navigate">
                    <span :class="isActive ? 'kerwinactive' : ''"
                        >即将上映</span
                    >
                </li>
            </router-link>
        </ul>

        <router-view></router-view>
    </div>
</template>

<script setup>
import { Swipe as vanSwipe, SwipeItem as vanSwipeItem } from "vant";
import { ref } from "vue";
const datalist = ref([
    {
        id: 1,
        imgUrl: "https://pic.maizuo.com/usr/movie/94d069d3e037bb221d7b4b581ccaff51.jpg",
        title: "海王2：失落的王国",
    },
    {
        id: 2,
        imgUrl: "https://pic.maizuo.com/usr/movie/88ea8dff563db98b06efcfc07acf5283.jpg",
        title: "三大队",
    },
    {
        id: 3,
        imgUrl: "https://pic.maizuo.com/usr/movie/b5ef931e6d7f3419dbc2e196afaf1fc7.jpg",
        title: "一闪一闪亮星星",
    },
]);
</script>

<style scoped lang="scss">
.header {
    display: flex;
    height: 50px;
    line-height: 50px;
    text-align: center;

    // 粘性定位，到top为0的时候sticky住，并且z轴在上面，不会被盖住，背景色白色，不会透视列表内容
    position: sticky;
    top: 0;
    z-index: 100;
    background: white;

    li {
        flex: 1;

        span {
            padding: 10px 0;
        }
    }
}
.kerwinactive {
    color: red;
    border-bottom: 3px solid red;
}
</style>
