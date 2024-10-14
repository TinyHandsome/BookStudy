<template>
    <div>
        child
        <button @click="handleClick">click</button>
        <button @click="$emit('myevent', childTitle)">click2</button>
    </div>
</template>

<script>
    export default {
        data(){
            return {
                childTitle: "child-111"
            }
        },
        methods: {
            handleClick(){
                this.$emit("myevent", this.childTitle)
            }
        }
    }
</script>

<style scoped>
    div {
        background: yellow;
    }
</style>