<template>
    <div>
        通信
        <navbar myname="home" myid="111" @event="change"></navbar>
        <sidebar v-show="obj.isShow"></sidebar>
    </div>
</template>

<script>
import navbar from './components/navbar'
import sidebar from './components/sidebar'
import { reactive } from "vue";
export default {
    components: {
        navbar,
        sidebar
    },

    setup() {
        const obj = reactive({
            isShow: true
        })

        const change = () => {
            obj.isShow = !obj.isShow
        }

        return {
            obj,
            change
        }
    }
}
</script>