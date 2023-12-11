<template>
    <div>Cinemas</div>
</template>

<script>
export default {
    beforeRouteLeave() {
        const answer = window.confirm("你确定要离开吗？");
        if (!answer) return false;
    },
};
</script>

<style scoped></style>
