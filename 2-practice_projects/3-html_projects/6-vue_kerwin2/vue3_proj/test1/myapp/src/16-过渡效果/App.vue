<template>
    <div>
        <button @click="isShow = !isShow">click</button>
        <Transition name="kerwin" mode="out-in" appear>
            <div v-if="isShow">111</div>
            <div v-else>321123</div>
        </Transition>
        <div>我是分割线</div>
        <Transition name="jun">
            <div v-show="isShow">222</div>
        </Transition>
        <div>我是分割线2</div>
        <Transition mode="out-in" enter-active-class="animate__bounceIn" leave-active-class="animate__bounceOut">
            <div v-if="isShow">333</div>
            <div v-else="isShow">444</div>
        </Transition>
    </div>
</template>

<script>
import 'animate.css'
export default {
    data() {
        return {
            isShow: true,
        };
    },
};
</script>

<style scoped>
.kerwin-enter-active, .kerwin-leave-active {
    /* transition: opacity 0.5s ease; */
    transition: all 0.5s ease;
}
.kerwin-enter-from, .kerwin-leave-to {
    opacity: 0;
    transform: translateX(100px);
}
.jun-enter-active{
    animation: junanimate 1s;
}
.jun-leave-active {
    animation: junanimate 1s reverse;
}

@keyframes junanimate {
    0% {
        transform: translateX(100px);
        opacity: 0;
    }
    100%{
        transform: translateX(0);
        opacity: 1;
    }
}

html, body {
    overflow-x: hidden;
}
</style>
