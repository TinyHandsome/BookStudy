<template>
    <div>
        <button v-show="left" @click="handleClick">返回</button>
        {{ title }}
        <button>首页</button>
    </div>
</template>

<script>
    export default {
        // props: ["title"],
        props: {
            title: String,
            left: Boolean
        },
        setup(props, {emit}){
            console.log(props.title);
            const handleClick = () => {
                console.log("click");
                emit("leftevent")
            }

            return {
                handleClick
            }
        }
    }
</script>

<style scoped>
    
</style>