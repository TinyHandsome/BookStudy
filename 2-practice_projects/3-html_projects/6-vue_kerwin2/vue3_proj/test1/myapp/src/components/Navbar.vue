<template>
    <div>
        <button @click="handleClick">展开/折叠 侧边栏</button>
        <div>vue3的单文件组件的演示</div>
    </div>
</template>

<script>
export default {
    methods: {
        handleClick(){
            console.log("click");
        }
    }
}
</script>


<style scoped>
    div{
        background: green;
    }   
</style>