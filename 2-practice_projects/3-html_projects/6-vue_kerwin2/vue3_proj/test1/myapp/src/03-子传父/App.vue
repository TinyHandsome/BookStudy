<template>
    <div>
        <Child @myevent="handleEvent"></Child>
    </div>
</template>

<script>
import Child from './Child.vue'
export default {
    components: {
        Child,
    },
    methods: {
        handleEvent(data){
            console.log(data);
        }
    }
}
</script>

<style scoped></style>