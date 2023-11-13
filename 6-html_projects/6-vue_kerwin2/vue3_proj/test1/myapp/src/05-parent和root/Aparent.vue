<template>
    <div>
        parent
        <BChild></BChild>
    </div>
</template>

<script>
import BChild from './BChild.vue';

    export default {
        data(){
            return {
                title: "parent-222"
            }
        },
        components:{
            BChild
        }
    }
</script> 

<style scoped>

</style>