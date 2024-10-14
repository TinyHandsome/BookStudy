<template>
    <div>
        <select v-model="type">
            <option :value="0">App订票</option>
            <option :value="1">前台兑换</option>
        </select>
        <ul>
            <li v-for="item in $store.getters.filterCinemaList(type)" :key="item.cinemaId">
                {{ item.name }}
            </li>
        </ul>
    </div>
</template>

<script>

export default {
    beforeRouteLeave() {
        const answer = window.confirm("你确定要离开吗？");
        if (!answer) return false;
    },
    data(){
        return {
            type: 1
        }
    },
    mounted() {
        if(this.$store.state.cinemaList.length === 0){
            // 如果store中没有数据，就去拿数据
            this.$store.dispatch('getCinemaList')
        }else{
            console.log("缓存");
        }
    },
    // computed: {
    //     filterCinemaList(){ 
    //         console.log(this.$store.state.cinemaList);
    //         console.log(this.type);
    //         return this.$store.state.cinemaList.filter(item => item.eTicketFlag===this.type)
    //     }
    // }
};
</script>

<style scoped>
li{
    padding: 2px
}
</style>
