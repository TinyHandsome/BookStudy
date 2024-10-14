<template>
    <div>
        <Transition :name="myname">
            <slot></slot>
        </Transition>
    </div>
</template>

<script>
    export default {
        props: ["myname"]
    }
</script>

<style scoped>
.l2r-enter-active{
    animation: kerwinanimate 1s;
}
.l2r-leave-active{
    animation: kerwinanimate 1s reverse;
}

.r2l-enter-active{
    animation: kerwinanimate2 1s;
}
.r2l-leave-active{
    animation: kerwinanimate2 1s reverse;
}

@keyframes kerwinanimate {
    0%{
        transform: translateX(-100px);
        opacity: 0;
    }
    100%{
        transform: translateX(0);
        opacity: 1;
    }
}
@keyframes kerwinanimate2 {
    0%{
        transform: translateX(100px);
        opacity: 0;
    }
    100%{
        transform: translateX(0);
        opacity: 1;
    }
}
</style>