<template>
    <div>1111</div>
    <div>
        todo
        {{ obj.mytext }}
        <input type="text" v-model="obj.mytext">

        <input type="text" ref="mytextref">

        <button @click="handleAdd">click</button>

        <ul>
            <li v-for="data in obj.datalist" :key="data">
                {{ data }}
            </li>
        </ul>
    </div>
</template>

<script>
import { reactive, ref } from "vue";
export default {
    mounted() {
        console.log("mounted", this.$refs.mytextref);
    },

    setup() {
        const obj = reactive({
            mytext: '',
            datalist: []
        })

        const mytextref = ref()

        const handleAdd = () => {
            console.log(obj.mytext);
            console.log(mytextref.value.value);
            obj.datalist.push(obj.mytext)
            obj.mytext = ''
        }

        return {
            obj,
            handleAdd,
            mytextref
        }
    }
}
</script>