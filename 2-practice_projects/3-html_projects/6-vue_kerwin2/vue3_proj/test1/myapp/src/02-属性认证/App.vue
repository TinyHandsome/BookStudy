<template>
    <div>
        <Navbar title="首页" left="返回" right="首页"
        leftshow="true" :rightshow="false"
        ></Navbar>
    </div>
</template>

<script>
import Navbar from './Navbar.vue';

export default {
    components: {
        Navbar
    }
}
</script>

<style></style>