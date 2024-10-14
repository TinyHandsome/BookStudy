<template>
    <div>
        <van-index-bar :index-list="indexlist">
            <div v-for="(item, index) in datalist" :key="item.type">
                <van-index-anchor :index="item.type" />
                <van-cell
                    v-for="x in item.list"
                    :key="x.cityId"
                    :title="x.name"
                    @click="handleClick(x)"
                />
            </div>
        </van-index-bar>
    </div>
</template>

<script setup>
import axios from "axios";
import { computed, onMounted, ref } from "vue";
import _ from "lodash";
import {
    IndexBar as vanIndexBar,
    IndexAnchor as vanIndexAnchor,
    Cell as vanCell,
} from "vant";
import useCityStore from "../store/cityStore";
import { useRouter } from "vue-router";

const router = useRouter()
const store = useCityStore();
const datalist = ref([]);
const indexlist = computed(() => {
    return datalist.value.map((item) => item.type);
});

onMounted(async () => {
    var res = await axios({
        url: "https://m.maizuo.com/gateway?k=7605862",
        headers: {
            "X-Client-Info":
                '{"a":"3000","ch":"1002","v":"5.2.1","e":"1701324144895711134613505"}',
            "X-Host": "mall.film-ticket.city.list",
        },
    });
    // console.log(res.data.data.cities);
    datalist.value = filterCity(res.data.data.cities);
});

// 方法1
const filterCity1 = (cities) => {
    var letterArr = [];
    for (let i = 65; i < 91; i++) {
        letterArr.push(String.fromCharCode(i));
    }
    var newCities = [];
    for (let index = 0; index < letterArr.length; index++) {
        newCities.push({
            type: letterArr[index],
            list: cities.filter(
                (item) =>
                    item.pinyin.substring(0, 1).toUpperCase() ===
                    letterArr[index]
            ),
        });
    }
    newCities = newCities.filter((item) => item.list.length);
    console.log(newCities);
};

// 方法2
const filterCity = (cities) => {
    // 分组，lodash，js增强，方法增强
    cities.sort(
        (item1, item2) =>
            item1.pinyin.substring(0, 1).toUpperCase().charCodeAt() -
            item2.pinyin.substring(0, 1).toUpperCase().charCodeAt()
    );
    var group_list = _.groupBy(cities, (item) =>
        item.pinyin.substring(0, 1).toUpperCase()
    );
    // console.log(111, group_list);

    var newCities = [];
    for (let i in group_list) {
        newCities.push({
            type: i,
            list: group_list[i],
        });
    }

    console.log(newCities);
    return newCities;
};

const handleClick = ({ name, cityId }) => {
    store.change(name, cityId);

    router.go(-1)
};
</script>

<style lang="scss" scoped></style>
