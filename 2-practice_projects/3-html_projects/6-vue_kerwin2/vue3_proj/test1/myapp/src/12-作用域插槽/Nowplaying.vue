<template>
    <div>
        <slot :mylist="datalist" a=1 b=2>
            <ul>
                <li v-for="item in datalist" :key="item.filmId">
                    {{ item.name }}
                </li>
            </ul>
        </slot>
    </div>
</template>

<script>
import axios from "axios";
export default {
    data() {
        return {
            datalist: [],
        };
    },
    mounted() {
        // console.log("mounted");
        // fetch("test.json")
        //     .then(res => res.json())
        //     .then(res => {
        //         console.log(res);
        //     })

        axios.get("test.json").then((res) => {
            // console.log(res.data.data.films);
            this.datalist = res.data.data.films;
        });
    },
};
</script>
<style scoped></style>
