<template>
    <div>
        <div ref="mydiv">测试</div>
        <div @click="handleClick">app-{{ myname }}-{{ computedName }}</div>
        <button @click="handleAdd">click</button>

        <input type="text" v-model="mytext" />

        <ul>
            <li v-for="(item, index) in list" :key="item">
                {{ index }} - {{ item }}
                <button @click="handleDel(index)">del</button>
            </li>
        </ul>

        <Child
            style="background: yellow"
            title="首页"
            :item="{
                name: 'kerwin',
                age: 100,
                list: [1, 2, 3],
            }"
            @event="handleEvent"
        ></Child>
    </div>
</template>

<script lang="ts">
import Child from "./Child.vue";
interface MyData {
    myname: string;
    myage: number;
    list: Array<string>;
    mytext: string;
}

export default {
    components: {
        Child,
    },
    data() {
        // 断言
        return {
            myname: "kerwin",
            myage: 100,
            list: [],
            mytext: "",
        } as MyData;
    },
    methods: {
        handleClick() {
            this.myname = this.myname.substring(0, 1);
            this.myage = 111;
            // 断言对象为任意类型
            console.log((this.$refs.mydiv as any).innerHTML);
        },
        handleAdd() {
            this.list.push(this.mytext);
        },
        handleDel(index: number) {
            this.list.splice(index, 1);
        },
        handleEvent(data: string) {
            console.log("click", data);
        },
    },
    computed: {
        computedName() {
            return (
                this.myname.substring(0, 1).toUpperCase() +
                this.myname.substring(1)
            );
        },
    },
};
</script>

<style scoped></style>
