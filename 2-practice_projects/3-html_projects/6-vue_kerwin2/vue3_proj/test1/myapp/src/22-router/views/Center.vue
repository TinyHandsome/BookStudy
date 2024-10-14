<template>
    <div>
        Center
    </div>
</template>

<script>
    export default {
        async beforeRouteEnter(to, from, next){
            let isAuthenticated = await localStorage.getItem("token")

            if (isAuthenticated) {
                next()
            }else{
                next({name: "Login"})
            }
        }
    }
</script>

<style scoped>

</style>