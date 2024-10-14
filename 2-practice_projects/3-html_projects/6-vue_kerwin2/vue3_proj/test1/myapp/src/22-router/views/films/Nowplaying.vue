<template>
    <div>
        <ul>
            <!-- 声明式 -->
            <!-- <router-link custom :to="`/detail/` + item.filmId" v-slot="{isActive, navigate}" v-for="item in datalist" :key="item.filmId">
                <li @click="navigate">
                    {{ item.name }}
                </li>
            </router-link> -->

            <!-- 编程式 -->
            <li v-for="item in datalist" :key="item.filmId" @click="handleClick(item.filmId)">
                {{ item.name }}
            </li>
        </ul>
    </div>
</template>

<script>
import axios from "axios";
export default {
    data(){
        return {
            datalist: []
        }
    },
    async mounted() {
        // fetch
        const res = await axios({
            url: "https://m.maizuo.com/gateway?cityId=110100&pageNum=1&pageSize=10&type=1&k=7564252",
            headers: {
                "X-Client-Info":
                    '{"a":"3000","ch":"1002","v":"5.2.1","e":"1701324144895711134613505"}',
                "X-Host": "mall.film-ticket.film.list",
            },
        })
        console.log(res.data);
        this.datalist = res.data.data.films
    },
    methods: {
        handleClick(id){
            console.log(id);

            // 编程式
            this.$router.push(`/detail/${id}`)
        }
    }
};

</script>

<style lang="scss" scoped>
ul {
    li {
        padding: 10px;
    }
}
</style>
