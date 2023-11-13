<template>
    <div>
        app
        <div v-kerwin>111</div>
        <div v-aa="'blue'">sss</div>
        <div v-bb="whichColor">sss</div>
        <div v-cc="ccc">sss</div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            whichColor: 'grey',
            ccc: 'red'
        }
    },
    directives: {
        aa: {
            mounted(el, binding) {
                console.log("当前节点插入到父节点的时候调用", el);
                el.style.background = binding.value;
            },
        },
        bb: {
            mounted(el, binding) {
                console.log("当前节点插入到父节点的时候调用", el);
                el.style.background = binding.value;
            },
        },
        cc(el, binding){
            el.style.background = binding.value
        }
    },
};
</script>

<style scoped></style>
