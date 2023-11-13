<template>
    <div>
        <div>{{ myvalue }}</div>
        <!-- <input type="text" v-model="myvalue">
        <input type="text" :value="myvalue" @input="myvalue=$event.target.value"> -->

        <!-- <Field label="用户名" :value="myvalue" @myevent="handleEvent"></Field> -->
        <!-- <Field label="用户名" v-model="myvalue"></Field> -->
        <Field label="用户名" v-model:kerwin="myvalue"></Field>

        <button @click="handleRegister">注册</button>
        <button @click="handleReset">重置</button>
    </div>
</template>

<script>
import Field from './Field.vue'
export default {
    data() {
        return {
            myvalue: "aaa"
        }
    },
    components: {
        Field
    },
    methods: {
        handleRegister(){
            console.log(this.myvalue);
        },
        handleReset(){
            console.log("reset");
            this.myvalue = ""
        },
        handleEvent(value){
            this.myvalue = value
        }
    }
}
</script>

<style scoped></style>