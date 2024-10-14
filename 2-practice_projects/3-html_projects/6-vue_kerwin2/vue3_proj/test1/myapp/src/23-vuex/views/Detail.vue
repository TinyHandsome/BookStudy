<template>
    <div>
        <button @click="handleBack">返回</button>
    </div>

    <h3>猜你喜欢</h3>
    <ul>
        <li @click="handleClick">
            电影1
        </li>
    </ul>
</template>

<script>
    export default {
        beforeMount(){
            // 隐藏
            // this.$store.state.isTabbarShow = false;
            // this.$store.commit("hideTabbar")
            this.$store.commit("changeTabbar", false)
        },
        beforeUnmount(){
            // this.$store.state.isTabbarShow = true;
            // this.$store.commit("showTabbar")
            this.$store.commit("changeTabbar", true)
        },
        mounted(){
            console.log("接受上一个页面传来的参数" + this.$route.params.filmId);
        },
        methods: {
            handleBack(){
                this.$router.back()
            },
            handleClick(){
                this.$router.push(`/detail/6789`)
            }
        },
        watch: {
            "$route.params": function(){
                console.log(this.$route.params.filmId);
            }
        }
    }
</script>

<style scoped>

</style>