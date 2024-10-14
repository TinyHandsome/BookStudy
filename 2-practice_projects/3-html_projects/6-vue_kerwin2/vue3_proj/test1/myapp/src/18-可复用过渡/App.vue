<template>
    <div>
        <button @click="isShow = !isShow">click</button>
        <KerwinTransition myname="r2l">
            <div v-if="isShow">111</div>
        </KerwinTransition>
        <KerwinTransition myname="l2r">
            <div v-if="isShow">111</div>
        </KerwinTransition>
    </div>
</template>

<script>
import KerwinTransition from "./KerwinTransition.vue";
export default {
    data() {
        return {
            isShow: true,
        };
    },
    components:{
        KerwinTransition
    }
};
</script>

<style scoped></style>
