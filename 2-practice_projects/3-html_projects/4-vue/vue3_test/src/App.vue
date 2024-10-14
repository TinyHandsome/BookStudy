<template>
    <div>
        <div style="background: yellow;" v-show="isShow">header</div>
        <ul v-show="$store.state.isTabbarShow">
            <router-link to="/films" custom v-slot="{ navigate, isActive }">
                <li @click="navigate" :class="isActive ? 'kerwinactive' : ''">
                    <i class="iconfont icon-all"></i>
                    <span>电影</span>
                </li>
            </router-link>
            <router-link to="/cinemas" custom v-slot="{ navigate, isActive }">
                <li @click="navigate" :class="isActive ? 'kerwinactive' : ''">
                    <i class="iconfont icon-all"></i>
                    <span>影院</span>
                </li>
            </router-link>
            <router-link to="/center" custom v-slot="{ navigate, isActive }">
                <li @click="navigate" :class="isActive ? 'kerwinactive' : ''">
                    <i class="iconfont icon-all"></i>
                    <span>我的</span>
                </li>
            </router-link>
        </ul>
        <router-view></router-view>
    </div>
</template>

<script>
import { provide } from "vue";
import { ref } from "vue";
export default {
    setup() {
        const isShow = ref(false)

        // 谁想用isShow，就把这个功能注入过来
        provide("kerwinshow", isShow)
        return {
            isShow
        }
    }
}
</script>

<style lang="scss" scoped>
.kerwinactive {
    color: red;
}
</style>