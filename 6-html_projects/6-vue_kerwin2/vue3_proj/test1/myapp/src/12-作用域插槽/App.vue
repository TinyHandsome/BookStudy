<template>
    <div>
        <input type="text" v-model="text"/>
        <Nowplaying v-slot="myprops">
            <ul>
                <li v-for="item in myprops.mylist" :key="item.filmId">
                    <!-- <img :src="item.poster" alt="" style="width: 100px" /> -->

                    <div v-if="item.name.includes(text) && text != ''" style="color: red">
                        {{ item.name }}
                    </div>
                    <div v-else>
                        {{ item.name }}
                    </div>
                </li>
            </ul>
        </Nowplaying>
    </div>
</template>

<script>
import Nowplaying from "./Nowplaying.vue";
export default {
    data(){
        return {
            text: ""
        }
    },
    components: {
        Nowplaying,
    },
};
</script>

<style scoped></style>
