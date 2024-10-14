<template>
    <div>
        nowplaying

        <ul v-show="$store.state.isTabbarShow">
            <li v-for="(item, index) in datalist" :key="item.filmId" @click="handleChangePage(item.filmId)">
                {{ item.name }}

                <div>{{ actorFilter(item.actors) }}</div>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from "axios";
import { onMounted, reactive, toRefs } from "vue";
import { useRouter } from "vue-router";
export default {

    setup() {

        // router === this.$router
        const router = useRouter()
        const obj = reactive({
            datalist: []
        })
        const handleChangePage = (id) => {
            router.push(`/detail/${id}`)
        }

        const actorFilter = (data) => {
            if (data === undefined) return "暂无主演";
            return data.map((item) =>
                item.name
            ).join(" ");
        }

        onMounted(() => {
            axios({
                url: "https://m.maizuo.com/gateway?cityId=440300&pageNum=1&pageSize=10&type=1&k=365658",
                headers: {
                    'X-Client-Info': '{"a":"3000","ch":"1002","v":"5.2.1","e":"1689149181904756335738881"}',
                    'X-Host': 'mall.film-ticket.film.list'
                }
            }).then(res => {
                obj.datalist = res.data.data.films
                console.log(obj.datalist);
            })
        })

        return {
            ...toRefs(obj),
            handleChangePage,
            actorFilter
        }
    }
}
</script>