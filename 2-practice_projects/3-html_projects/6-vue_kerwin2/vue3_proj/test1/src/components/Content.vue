<template>
    <div>
        content
        <button @click="handleClick">click</button>
    </div>
</template>

<script>
    export default {
        methods: {
            handleClick(){
                console.log("click");
            }
        }
    }
</script>   

<style lang="scss" scoped>

</style>