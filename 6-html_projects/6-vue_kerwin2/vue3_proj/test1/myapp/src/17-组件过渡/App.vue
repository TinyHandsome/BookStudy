<template>
    <div>
        <Navbar></Navbar>

        <!-- <Home v-if="which==='首页'"></Home>
        <List v-else-if="which==='列表'"></List>
        <Center v-else></Center> -->

        <!-- 内置的动态组件 -->
        <keep-alive>
            <Transition name="jun" mode="out-in">
                <component :is="which"></component>
            </Transition>
        </keep-alive>

        <Tabbar></Tabbar>

        <input type="text" v-model="mytext" />
        <button @click="handleAdd">add</button>
        <!-- <ul> -->
        <TransitionGroup tag="ul" name="jun">
            <li v-for="(item, index) in items" :key="item">
                {{ item }}
                <button @click="handleDel(index)">del</button>
            </li>
        </TransitionGroup>
        <!-- </ul> -->
    </div>
</template>

<script>
import Navbar from "./Navbar.vue";
import Tabbar from "./Tabbar.vue";
import store from "./store";
import Center from "./views/Center.vue";
import Home from "./views/Home.vue";
import List from "./views/List.vue";
export default {
    data() {
        return {
            navTitle: "我的首页",
            which: "Home",
            mytext: "",
            items: [],
        };
    },
    methods: {
        handleAdd() {
            this.items.push(this.mytext);
            this.mytext = "";
        },
        handleDel(index) {
            this.items.splice(index, 1);
        },
    },
    provide() {
        return {
            navTitle: this.navTitle,
            app: this,
        };
    },
    mounted() {
        var obj = {
            首页: "Home",
            列表: "List",
            我的: "Center",
        };
        store.subscribe((value) => {
            // 列表 list
            // 首页 Home
            // 我的 Center
            this.which = obj[value];
        });
    },
    components: {
        Navbar,
        Tabbar,
        Home,
        List,
        Center,
    },
};
</script>

<style>
* {
    margin: 0;
    padding: 0;
}

ul {
    list-style: none;
}

.kerwin-enter-active,
.kerwin-leave-active {
    /* transition: opacity 0.5s ease; */
    transition: all 0.5s ease;
}
.kerwin-enter-from,
.kerwin-leave-to {
    opacity: 0;
    transform: translateX(100px);
}
.jun-enter-active {
    animation: junanimate 1s;
}
.jun-leave-active {
    animation: junanimate 1s reverse;
}

@keyframes junanimate {
    0% {
        transform: translateX(100px);
        opacity: 0;
    }
    100% {
        transform: translateX(0);
        opacity: 1;
    }
}

html,
body {
    overflow-x: hidden;
}
/* 李彪上来的速度 */
.jun-move {
    transition: all 0.5s ease;
}
/* 确保将离开的元素从布局流中删除，以便能够正确的计算移动的动画 */
.jun-leave-active {
    position: absolute;
}
</style>
