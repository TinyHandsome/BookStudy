<template>
    <div>
        child- <button @click="handleClick">click</button>
    </div>
</template>

<script>
    export default {
        methods: {
            handleClick(){
                console.log(this.$parent.title);
                console.log(this.$parent.$parent.title);
            }
        }
    }
</script>

<style scoped>

</style>