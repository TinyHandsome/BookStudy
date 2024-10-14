<template>
    <div>
        <input type="text" ref="mytext">
        <button @click="handleAdd">add</button>

        <ul>
            <li v-for="data in datalist" :key="data">
                {{ data }}
            </li>
        </ul>
    </div>
</template>

<script>
import { ref } from "vue";
export default {
    setup() {
        const mytext = ref()
        const datalist = ref([111, 222])

        const handleAdd = () => {
            console.log(mytext.value.value);
            datalist.value.push(mytext.value.value)
            mytext.value.value = ''
        }

        return {
            handleAdd,
            mytext,
            datalist
        }
    }
}
</script>