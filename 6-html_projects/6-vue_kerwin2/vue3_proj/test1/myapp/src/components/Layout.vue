<template>
    <div>
        <Sidebar v-if="isShow"></Sidebar>
        <Content></Content>
    </div>
</template>

<script>
import Content from './Content.vue'
import Sidebar from './Sidebar.vue'
export default {
    data(){
        return {
            isShow: true
        }
    },
    components: {
        Content,
        Sidebar
    }
}
</script>