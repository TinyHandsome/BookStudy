<template>
    <div>child-{{ props.obj?.age }}</div>
    <button @click="handleClick">click</button>
</template>

<script setup lang="ts">
// const props = defineProps({
//     title: String,
//     obj: Object
// })

interface IProps {
    name: string;
    age: number;
}

const props = defineProps<{
    title: string;
    obj: IProps;
}>();

// const emit = defineEmits(["ee"])
const emit = defineEmits<{
    (e: "ee", myvalue: string): void;
}>();
const handleClick = () => {
    emit("ee", "hello");
};
</script>

<style scoped></style>
