<template>
    <div>
        <Navbar></Navbar>

        <!-- <Home v-if="which==='首页'"></Home>
        <List v-else-if="which==='列表'"></List>
        <Center v-else></Center> -->

        <!-- 内置的动态组件 -->
        <keep-alive>
            <component :is="which"></component>
        </keep-alive>

        <Tabbar></Tabbar>
    </div>
</template>

<script>
import Navbar from './Navbar.vue'
import Tabbar from './Tabbar.vue';
import store from './store';
import Center from './views/Center.vue';
import Home from './views/Home.vue';
import List from './views/List.vue';
export default {
    data() {
        return {
            navTitle: "我的首页",
            which: "Home",
        }
    },
    provide() {
        return {
            navTitle: this.navTitle,
            app: this
        }
    },
    mounted() {
        var obj = {
            "首页": "Home",
            "列表": "List",
            "我的": "Center",
        }
        store.subscribe((value) => {
            // 列表 list
            // 首页 Home
            // 我的 Center
            this.which = obj[value]
        })
    },
    components: {
        Navbar,
        Tabbar,
        Home,
        List,
        Center
    }
}
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