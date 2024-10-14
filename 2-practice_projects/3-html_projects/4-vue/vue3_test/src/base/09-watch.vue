<template>
    <div>
        <input type="text" v-model="obj.mytext">
        <ul>
            <li v-for="data in obj.datalist" :key="data">
                {{ data }}
            </li>
        </ul>
    </div>
</template>

<script>
import { reactive, watch } from "vue";
export default {
    setup() {
        const obj = reactive({
            mytext: '',
            datalist: ["aaa", "bbb", "ccc", "bcc", "bcd", "abb"],
            oldlist: ["aaa", "bbb", "ccc", "bcc", "bcd", "abb"]
        })

        watch(() => obj.mytext, () => {
            console.log("watch");
            obj.datalist = obj.oldlist.filter(item => item.includes(obj.mytext))
        })

        return {
            obj
        }
    }
}
</script>