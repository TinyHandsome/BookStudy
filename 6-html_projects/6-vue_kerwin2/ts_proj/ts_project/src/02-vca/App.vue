<template>
    <div>app-{{ state.myname }}</div>
    <div>computed-{{ computedName }}</div>

    <div ref="mydiv">我是div</div>

    <Child
        title="首页"
        :obj="{
            age: 100,
            name: 'kewin',
        }"
        @ee="handleEvent"
    ></Child>
</template>

<script setup lang="ts">
import { reactive, ref, onMounted, computed } from "vue";
import type { Ref } from "vue";
import Child from "./Child.vue";

interface IState {
    myname: string;
}

const state: IState = reactive({
    myname: "kerwin",
});

const cc: Ref<string> = ref("leetyan");
const dd = ref<string>("dd");

const mydiv = ref<HTMLDivElement>();
onMounted(() => {
    console.log(mydiv.value?.innerHTML);
});

const computedName = computed<string>(
    () =>
        cc.value.substring(0, 1).toUpperCase() +
        cc.value.substring(1).toLowerCase()
);

const handleEvent = (value: string) => {
    console.log(value);
};
</script>

<style scoped></style>
