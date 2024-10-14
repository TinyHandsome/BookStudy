<template>
    <div>
        app
        <Child>
            <template v-slot:one>
                <div>我是app组件重的div</div>
            </template>
            <template #two>
                <div>我是插槽2</div>
            </template>

            <div>3333</div>
        </Child>
    </div>
</template>

<script>
import Child from './Child.vue';

export default {
    components: {
        Child,
    }
}
</script>

<style scoped></style>