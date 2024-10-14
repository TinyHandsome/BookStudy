<template>
    <div>
        <!-- <ul>
            <li v-for="item in items" :key="item.id">
                {{ item }}
            </li>
        </ul> -->
        <ul>
            <TabbarItem v-for="data in items" :key="data" :item="data">
            </TabbarItem>
        </ul>
    </div>
</template>

<script>
import TabbarItem from './TabbarItem.vue';
export default {
    data() {
        return {
            items: ["首页", "列表", "我的"]
        }
    },
    components: {
        TabbarItem
    }
}
</script>

<style scoped>
ul {
    display: flex;
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 50px;
    line-height: 50px;
}

li {
    flex: 1;
    text-align: center;
}
</style>