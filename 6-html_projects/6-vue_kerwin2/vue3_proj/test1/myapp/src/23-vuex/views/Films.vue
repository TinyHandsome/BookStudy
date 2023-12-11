<template>
    <div>
        <div style="height: 100px; line-height: 100px; text-align: center">
            大轮播
        </div>

        <ul class="header">
            <router-link to="/films/nowplaying" custom v-slot="{ isActive, navigate }">
                <li @click="navigate">
                    <span :class="isActive?'kerwinactive':''">正在热映</span>
                </li>
            </router-link>
            <router-link to="/films/comingsoon" custom #="{ isActive, navigate }">
                <li @click="navigate"><span :class="isActive?'kerwinactive':''">即将上映</span></li>
            </router-link>
        </ul>

        <router-view></router-view>
    </div>
</template>

<script>
export default {};
</script>

<style scoped lang="scss">
.header {
    display: flex;
    height: 50px;
    line-height: 50px;
    text-align: center;
    li {
        flex: 1;

        span {
            padding: 10px 0;
        }
    }
}
.kerwinactive {
    color: red;
    border-bottom: 3px solid red;
}
</style>
