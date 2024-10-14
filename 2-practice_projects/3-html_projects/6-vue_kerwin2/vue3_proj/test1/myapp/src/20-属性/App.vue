<template>
    <div>
        <Navbar title="首页" :left="true" @leftevent="handleLeft"></Navbar>
        <Navbar title="影院" :left="false"></Navbar>
    </div>
</template>

<script>
import Navbar from './Navbar.vue'
    export default {
        components: {
            Navbar
        },

        setup(){
            const handleLeft = () => {
                console.log("left button");
            }

            return {
                handleLeft
            }
        }
    }
</script>

<style scoped>

</style>