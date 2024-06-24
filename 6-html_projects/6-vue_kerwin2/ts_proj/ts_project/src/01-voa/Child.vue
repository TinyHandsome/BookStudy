<template>
    <div>child-{{ title }}</div>
    {{ item?.name }}
    {{ item?.age }}

    <button @click="handleClick">子</button>
</template>

<script lang="ts">
import type { PropType } from "vue";

interface IProps{
    name: string,
    age: number,
    list: Array<string>
}

export default {
    props: {
        title: String,
        item: Object as PropType<IProps>,
    },
    methods: {
        handleClick(){
            // 子传父
            this.$emit("event", "aaa")
        }
    },
    emits: {
        event(payload:string){
            return payload
        }
    }
};
</script>

<style scoped></style>
