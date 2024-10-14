<template>
    <div>
        <input type="text" v-model="obj.mytext">
        <ul>
            <li v-for="data in computedList" :key="data">
                {{ data }}
            </li>
        </ul>
    </div>
</template>

<script>
import { reactive, computed } from "vue";
export default {
    setup() {
        const obj = reactive({
            mytext: '',
            datalist: ["aaa", "bbb", "ccc", "bcc", "bcd", "abb"]
        })

        const computedList = computed(() => {
            return obj.datalist.filter(item => item.includes(obj.mytext))
        })

        return {
            obj,
            computedList
        }
    }
}
</script>