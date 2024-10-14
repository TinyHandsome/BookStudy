<template>
    <div>
        detail
    </div>
</template>

<script>
import { onMounted, onUnmounted, inject } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
export default {
    // mounted() {
    //     this.$store.commit("hide")
    //     console.log(this.$route.params.id);
    // },
    // unmounted() {
    //     this.$store.commit("show")
    // },

    setup() {
        // route === this.$route
        const route = useRoute()
        // store === this.$store
        const store = useStore()

        const isShow = inject("kerwinshow")

        onMounted(() => {
            console.log(route.params.id);
            store.commit("hide")
            isShow.value = false
        })
        onUnmounted(() => {
            store.commit("show")
            isShow.value = true
        })
    }
}
</script>