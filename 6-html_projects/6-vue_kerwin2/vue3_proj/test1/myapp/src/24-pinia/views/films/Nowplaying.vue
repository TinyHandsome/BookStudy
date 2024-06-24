<template>
    <div>
        <van-list
            v-model:loading="loading"
            :finished="finished"
            finished-text="没有更多了"
            @load="onLoad"
            :immediate-check="false"
            :offset="10"
        >
            <van-cell
                v-for="item in datalist"
                :key="item.filmId"
                @click="handleClick(item.filmId)"
            >
                <img
                    :src="item.poster"
                    alt=""
                    style="width: 100px; float: left"
                />
                <div>{{ item.name }}</div>
            </van-cell>
        </van-list>
    </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

import { List as vanList, Cell as vanCell } from "vant";

// 加载状态
const loading = ref(false);
// 结束状态
const finished = ref(false);

const datalist = ref([]);
const router = useRouter();

// 状态
const pageNum = ref(1);
const total = ref(0);

onMounted(async () => {
    // fetch
    const res = await axios({
        url: `https://m.maizuo.com/gateway?cityId=110100&pageNum=${pageNum.value}&pageSize=10&type=1&k=7564252`,
        headers: {
            "X-Client-Info":
                '{"a":"3000","ch":"1002","v":"5.2.1","e":"1701324144895711134613505"}',
            "X-Host": "mall.film-ticket.film.list",
        },
    });
    console.log(res.data);
    datalist.value = res.data.data.films;
    total.value = res.data.data.total;
});
const handleClick = (id) => {
    console.log(id);
    // 编程式
    router.push(`/detail/${id}`);
};

const onLoad = async () => {
    if (total.value === datalist.value.length){
        // 数据取完了
        finished.value = true
        return
    }


    console.log("到底了");
    pageNum.value++;

    const res = await axios({
        url: `https://m.maizuo.com/gateway?cityId=110100&pageNum=${pageNum.value}&pageSize=10&type=1&k=7564252`,
        headers: {
            "X-Client-Info":
                '{"a":"3000","ch":"1002","v":"5.2.1","e":"1701324144895711134613505"}',
            "X-Host": "mall.film-ticket.film.list",
        },
    });

    // 追加数据
    datalist.value = [...datalist.value, ...res.data.data.films];
    // loading修改
    loading.value = false;
};
</script>

<style lang="scss" scoped>
ul {
    li {
        padding: 10px;
    }
}

:deep(.van-cell__value) {
    text-align: left;
}
</style>
