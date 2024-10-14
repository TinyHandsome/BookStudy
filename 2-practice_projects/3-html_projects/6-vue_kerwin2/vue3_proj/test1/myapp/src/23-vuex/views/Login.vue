<template>
    <div>
        <span> Login-  </span>
        <button @click="handleLogin">登录</button>
    </div>
</template>

<script>
    export default {
        methods: {
            handleLogin(){
                localStorage.setItem("token", "aaa")
                this.$router.push('/')
            }
        }
    }
</script>

<style scoped>

</style>