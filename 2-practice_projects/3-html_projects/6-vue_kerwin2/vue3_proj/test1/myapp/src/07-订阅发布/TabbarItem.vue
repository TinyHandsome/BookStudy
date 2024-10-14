<template>
    <li @click="handleClick">
        {{ item }}
    </li>
</template>

<script>
import store from './store';

    export default {
        props: ["item"],
        methods: {
            handleClick(){
                // console.log(this.navTitle);
                store.publish(this.item)
            }
        }
    }
</script>

<style scoped>

</style>