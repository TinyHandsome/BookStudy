<template>
    <div style="background-color: yellow;">
        {{ myvalue }}
        <label>{{ label }}</label>
        <input :type="type" v-model="myvalue">
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
            type: {
                type: String,
                default: "text"
            }
        }
    }
</script>

<style scoped>

</style>