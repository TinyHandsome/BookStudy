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

<script setup>
import { onMounted, onBeforeMount, onBeforeUnmount } from 'vue';
import { useRoute, useRouter, onBeforeRouteUpdate } from 'vue-router';
import useTabbarStore from '../store/tabbarStore';
const route = useRoute()
const router = useRouter()
const store = useTabbarStore()

onMounted(() => {
    console.log("接受上一个页面传来的参数" + route.params.filmId);
})

onBeforeMount(() => {
    // store.isTabbarShow = false
    // store.$patch({
    //     isTabbarShow: false
    // })
    store.change(false)
})

onBeforeUnmount(() => {
    // store.isTabbarShow = true
    // store.$patch({
    //     isTabbarShow: true
    // })
    // store.$reset()
    store.change(true)
})

const handleBack = () => {
    router.back()
}
const handleClick = () => {
    router.push(`/detail/6789`)
}
    //     watch: {
    //         "$route.params": function(){
    //             console.log(this.$route.params.filmId);
    //         }
    //     }
    // }
</script>

<!-- <script>
import useTabbarStore from '../store/tabbarStore';
import {mapState, mapActions} from 'vuex'

export default {
    computed: {
        ...mapState(useTabbarStore, ["isTabbarShow"])
    },
    methods: {
        ...mapActions(useTabbarStore, ["change"])
    }

}
</script> -->

<style scoped>

</style>