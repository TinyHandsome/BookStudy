<template>
    <div>
        app
        <Navbar></Navbar>
        <Tabbar></Tabbar>
    </div>
</template>

<script>
import Navbar from './Navbar.vue'
import Tabbar from './Tabbar.vue';
    export default {
        data(){
            return {
                navTitle: "我的首页"
            }
        },
        provide(){
            return {
                navTitle: this.navTitle,
                app: this
            }
        },
        components: {
            Navbar,
            Tabbar
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