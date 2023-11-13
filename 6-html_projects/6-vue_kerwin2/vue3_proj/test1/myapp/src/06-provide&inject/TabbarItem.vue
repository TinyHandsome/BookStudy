<template>
    <li @click="handleClick">
        {{ item }}
    </li>
</template>

<script>
    export default {
        props: ["item"],
        inject: ["navTitle", "app"],
        methods: {
            handleClick(){
                // console.log(this.navTitle);
                this.app.navTitle = this.item
            }
        }
    }
</script>

<style scoped>

</style>