<template>
    <div>
        app
        <div>{{ obj.myname }}</div>
        <div>{{ obj.myage }}</div>
        <button @click="handleClick">click</button>

        <div>
            <input type="text" v-model="state.mytext" />
            <button @click="hClick">add</button>
            <ul>
                <li v-for="(item, index) in state.datalist" :key="item">
                    {{ item }}
                    <button @click="handleDel(index)">删除</button>
                </li>
            </ul>
        </div>

        <div>
            <input type="text" ref="myinput">
        </div>

        <div>
            <input type="text" v-model="anotext">
        </div>
        <select name="" id="" v-model="select">
            <option value="aaa">aaa</option>
            <option value="bbb">bbb</option>
            <option value="ccc">ccc</option>
        </select>


    </div>
</template>

<script>
import { reactive, ref, toRef, watch } from "vue";

export default {
    setup() {
        // 函数式编程
        const obj = reactive({
            myname: "kerwin",
            myage: 100,
        });
        const handleClick = () => {
            obj.myname = "kkkkkk";
            obj.myage = 18;
        };

        // reactive
        const state = reactive({
            mytext: "",
            datalist: ["111", "222", "333"],
        });
        const hClick = () => {
            state.datalist.push(state.mytext)
            state.mytext = ""
            console.log(myinput.value);
            console.log(myinput.value.value);
        }
        const handleDel = (index) => {
            state.datalist.splice(index, 1)
        }

        // ref
        const myinput = ref(null)

        // watch
        const anotext = ref("")
        watch(anotext, (newValue, oldValue) => {
            console.log("同步/异步", ": ", newValue, "-", oldValue);
        })
        const select = ref("bbb")
        watch([anotext, select], (newValue, oldValue) => {
            console.log("同步/异步", ": ", newValue, "-", oldValue);
        }, {immediate:true})

        return {
            obj,
            handleClick,
            state,
            hClick,
            handleDel,
            myinput,
            anotext,
            select
        };
    },
};
</script>

<style scoped></style>
