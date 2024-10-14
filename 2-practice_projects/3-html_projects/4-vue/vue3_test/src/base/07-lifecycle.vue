<template>
    <div>
        生命周期
        <ul>
            <li v-for="data in obj.list" :key="data">
                {{ data }}
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'
import { onBeforeMount, onMounted, reactive } from "vue";
export default {
    // mounted
    setup() {
        const obj = reactive({
            list: []
        })
        onBeforeMount(() => {
            console.log("上树之前就执行啦");
        })
        onMounted(() => {
            console.log("dom上树", "axiox，事件监听啊，setInterval启动啊啥的");
            setTimeout(() => {
                obj.list = ["aaa", "bbb"]
            }, 2000);
        })

        return { obj }
    }
}
</script>