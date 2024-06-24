<template>
    <div>
        {{ props.title }}
    </div>
</template>

<script setup>
import { defineProps } from 'vue'; 
const props = defineProps(["title"])
</script>

<style scoped>

</style>