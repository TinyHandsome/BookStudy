<template>
    <div>
        app
        <button @click="handleClick">click</button>
        <input ref="myinput">
        <Child ref="myChild"></Child>

        <Field label="用户名" type="text" ref="username"></Field>
        <Field label="密码" type="password" ref="password"></Field>
        <Field label="年龄" type="number" ref="age"></Field>

        <div>
            <button @click="register">注册</button>
            <button @click="reset">重置</button>
        </div>
    </div>
</template>

<script>
import Child from "./Child.vue"
import Field from "./Field.vue";
export default {
    components: {
        Child,
        Field
    },
    methods: {
        handleClick() {
            console.log(this.$refs.myinput);
            console.log(this.$refs.myChild);
            this.$refs.myChild.childtitle = "junjun"
        },
        register(){
            console.log(this.$refs.username.myvalue);
        },
        reset(){
            this.$refs.username.myvalue = ""
            this.$refs.password.myvalue = ""
            this.$refs.age.myvalue = ""
        }
    }
}
</script>

<style scoped></style>