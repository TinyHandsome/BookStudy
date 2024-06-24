<template>
    <div>
        <!-- 路由插槽 -->
        <router-view></router-view>

        <Tabbar v-show="store.isTabbarShow"></Tabbar>
    </div>
</template>

<script setup>
// import { storeToRefs } from "pinia";
import Tabbar from "./components/Tabbar.vue";
import useTabbarStore from "./store/tabbarStore";

const store = useTabbarStore();
console.log(store);

// store是一个reactive包装的对象，直接结构可以拿到里面的值，但是会失去响应式
// const { isTabbarShow } = store;
// const { isTabbarShow } = storeToRefs(store);
</script>

<style>
* {
    margin: 0;
    padding: 0;
}
ul {
    list-style: none;
}
</style>
