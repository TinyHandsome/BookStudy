<template>
    <div>
        <Navbar title="首页" left="返回" right="首页"></Navbar>
        <Navbar v-bind="{
            title: 'aaa',
            'left': 'l',
            'right': 'r'
        }"></Navbar>
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