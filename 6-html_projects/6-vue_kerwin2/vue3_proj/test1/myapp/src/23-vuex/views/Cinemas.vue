<template>
    <div>
        <ul>
            <li v-for="item in $store.state.cinemaList" :key="item.cinemaId">
                {{ item.name }}
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    beforeRouteLeave() {
        const answer = window.confirm("你确定要离开吗？");
        if (!answer) return false;
    },
    mounted() {
        if(this.$store.state.cinemaList.length === 0){
            // 如果store中没有数据，就去拿数据
            this.$store.dispatch('getCinemaList')
        }else{
            console.log("缓存");
        }
    }
};
</script>

<style scoped>
li{
    padding: 2px
}
</style>
