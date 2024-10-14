<template>
    <div class="tabbar">
        <ul>
            <!-- <router-link to="/films">电影</router-link>
            <router-link to="/cinemas">影院</router-link>
            <router-link to="/center">我的</router-link> -->

            <!-- 定制router-link为指定的节点 -->
            <router-link to="/films" custom v-slot="{isActive, navigate}">
                <li :class="isActive" @click="navigate">电影</li>
            </router-link>
            <router-link to="/cinemas" custom #="{isActive, navigate}">
                <li :class="isActive" @click="navigate">影院</li>
            </router-link>
            <router-link to="/center" custom #="{isActive, navigate}">
                <li :class="isActive" @click="navigate">我的</li>
            </router-link>
        </ul>
    </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.tabbar {
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 50px;
    line-height: 50px;
    text-align-last: center;
    background: white;
    z-index: 100;

    ul {
        display: flex;

        li {
            flex: 1;
        }
    }
}
// .tabbar ul {
//     display: flex;
// }
// .tabbar ul li {
//     flex: 1;
// }
</style>
