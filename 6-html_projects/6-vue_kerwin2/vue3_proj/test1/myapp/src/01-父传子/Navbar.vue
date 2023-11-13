<template>
    <div>
        <button>{{ left }}</button>
        aa-{{ title }}
        <button>{{ right }}</button>
    </div>
</template>

<script>
export default {
    props: ["title", "left", "right"]
}
</script>

<style scoped></style>

