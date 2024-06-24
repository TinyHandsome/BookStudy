<template>
    <div>
        Center
        <van-button type="primary" size="mini" :disabled="true">主要按钮</van-button>
        <van-button type="danger" :loading="ll" @click="hanldeClick">危险按钮</van-button>

        <div>element-plus demo</div>
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    async beforeRouteEnter(to, from, next) {
        let isAuthenticated = await localStorage.getItem("token");

        if (isAuthenticated) {
            next();
        } else {
            next({ name: "Login" });
        }
    },
    data(){
        return {
            ll: false,
        }
    },
    methods: {
        hanldeClick(){
            console.log("click");
            this.ll = true
        }
    }
};
</script>

<script setup>
import { Button } from "vant";
</script>

<style scoped></style>
