<template>
    <div>

        <!-- 路由插槽 -->
        <router-view></router-view>

        <Tabbar v-show="isTabbarShow"></Tabbar>
    </div>
</template>

<script>
import Tabbar from './components/Tabbar.vue';
import {mapState} from 'vuex';

export default {
    components: {
        Tabbar
    },
    mounted(){
        console.log(this.$store.state.isTabbarShow);
    },
    computed: mapState(['isTabbarShow'])
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