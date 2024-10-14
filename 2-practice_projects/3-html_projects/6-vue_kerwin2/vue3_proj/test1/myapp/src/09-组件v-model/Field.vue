<template>
    <div style="background-color: yellow;">
        <label>{{ label }}</label>
        <!-- <input :type="type" :value="value" @input="handleInput"> -->
        <!-- <input :type="type" :value=modelValue @input="handleInput"> -->

        <input :type="type" :value=kerwin @input="handleKerwin">
    </div>
</template>

<script>
    export default {
        data(){
            return {
                myvalue: ""
            }
        },
        props: {
            label: {
                type: String,
                default: ""
            },
            modelValue:{
                type: String,
                default: ""
            },
            kerwin:{
                type: String,
                default: ""
            },
            // value:{
            //     type: String,
            //     default: ""
            // },
            type: {
                type: String,
                default: "text"
            }
        },
        methods: {
            handleInput(evt){
                this.$emit("update:modelValue", evt.target.value)
            },
            handleKerwin(evt){
                this.$emit("update:kerwin", evt.target.value)
            }
            // handleInput(evt){
            //     this.$emit("myevent", evt.target.value)
            // }
        }
    }
</script>

<style scoped>

</style>