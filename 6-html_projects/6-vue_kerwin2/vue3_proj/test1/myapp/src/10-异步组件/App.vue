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
import { defineAsyncComponent } from 'vue';
import LoadingComponent from './components/LoadingComponent.vue'
import ErrorComponent from './components/ErrorComponent.vue'
import Navbar from './Navbar.vue'
import Tabbar from './Tabbar.vue';
import store from './store';
// import Center from './views/Center.vue';
// import Home from './views/Home.vue';
// import List from './views/List.vue';
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
        Home: defineAsyncComponent(() => import('./views/Home.vue')),
        List: defineAsyncComponent(() => import('./views/List.vue')),
        Center: defineAsyncComponent({
            // 加载函数
            loader: () => import('./views/Center.vue'),
            // 加载异步组件时使用的组件
            loadingComponent: LoadingComponent,
            // 展示加载组件前的延迟时间，默认为200ms
            delay:200,
            // 加载失败后展示的组件
            errorComponent: ErrorComponent,
            // 如果提供了一个timeout时间限制，并超时了
            // 也会显示这里配置的报错组件，默认是：Infinity
            timeout: 2000
        }),
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