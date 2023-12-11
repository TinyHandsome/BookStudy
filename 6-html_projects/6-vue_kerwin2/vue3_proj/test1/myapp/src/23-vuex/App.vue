<template>
    <div>

        <!-- 路由插槽 -->
        <router-view></router-view>

        <Tabbar v-show="$store.state.isTabbarShow"></Tabbar>
    </div>
</template>

<script>
import Tabbar from './components/Tabbar.vue';

export default {
    components: {
        Tabbar
    },
    mounted(){
        console.log(this.$store.state.isTabbarShow);
    }
}
</script>

<style>
*{
    margin: 0;
    padding: 0;
}
ul{
    list-style: none;
}
</style>