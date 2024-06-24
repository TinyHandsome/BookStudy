<template>
    <div>
        <van-nav-bar title="影院">
            <template #left>
                <div @click="handleChange">{{ cityStore.cityName }}</div>
            </template>
            <template #right>
                <van-icon name="search" size="22" color="black" />
            </template>
        </van-nav-bar>

        <select name="" id="" v-model="type">
            <option :value="1">APP订票</option>
            <option :value="0">前台兑换</option>
        </select>
        <ul>
            <li
                v-for="item in store.filterCinemaList(type)"
                :key="item.cinemaId"
            >
                {{ item.name }}
            </li>
        </ul>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import useCinemaStore from "../store/cinemaStore";
import useCityStore from '../store/cityStore'
import { NavBar as vanNavBar, Icon as vanIcon } from "vant";
import { useRouter } from "vue-router";

const router = useRouter()
const type = ref(1);
const store = useCinemaStore();
const cityStore = useCityStore()
onMounted(() => {
    if (store.cinemaList.length === 0) {
        // 如果store中没有数据，就去拿数据
        store.getCinemaList();
    } else {
        console.log("缓存");
    }
});

const handleChange = () => {
    router.push("/city");
    // 清空影院数据
    store.clearCinemaList()
};
</script>

<style scoped>
li {
    padding: 2px;
}
</style>
