<template>
    <div>
        <button>返回</button>
        <h3>{{ title }}</h3>
        <button>首页</button>
    </div>
</template>

<script>
import store from './store'
    export default {
        // inject: ["navTitle", "app"],
        data(){
            return {
                title: "首页",
            }
        },
        mounted(){
            console.log(111);
            store.subscribe((value) => {
                console.log("我被触发了");
                this.title = value
            })
        }
    }
</script>

<style scoped>
div {
    display: flex;
    width: 100%;
    justify-content: space-between;
    height: 50px;
    line-height: 50px;
    background: gray;
}
</style>