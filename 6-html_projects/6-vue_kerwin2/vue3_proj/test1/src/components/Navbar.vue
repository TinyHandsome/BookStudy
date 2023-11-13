<template>
    <div>
        navbar
        <button @click="handleClick">Click</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            mytext: "",
        };
    },
    methods: {
        handleClick() {
            console.log("111");
        },
    },
};
</script>

<style lang="scss" scoped></style>
