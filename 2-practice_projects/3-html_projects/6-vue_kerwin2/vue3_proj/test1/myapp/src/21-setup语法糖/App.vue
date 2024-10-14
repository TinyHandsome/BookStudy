<template>
    <div>
        app-{{ msg }}
        <button @click="handleClick">click</button>
        <div>{{ state.myname }} -- {{ state.myage }}</div>
    </div>
</template>

<script setup>
import {ref, reactive} from 'vue'
let msg = ref("hellow world")
const state = reactive({
    myname: "jj",
    myage: 100
})

const handleClick = () => {
    console.log(msg);
    msg.value = "hello kerwin"
    state.myname = "qwe"
    state.myage = 123
}
</script>

<style lang="scss" scoped>

</style>