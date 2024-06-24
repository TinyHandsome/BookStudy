<template>
    <!-- <div>
        Home
        <el-button type="primary">primary</el-button>
        <el-button type="success">success</el-button>
        <el-button type="info">info</el-button>
        <el-button type="warning">warning</el-button>
        <el-button type="danger">danger</el-button>
        <el-button>el的按钮</el-button>
    </div> -->
    <el-container class="layout-container-demo" style="height: 500px">
        <el-aside width="200px">
            <el-scrollbar>
                <el-menu :router="true" :default-active="route.fullPath">
                    <el-menu-item index="/home">
                        <el-icon><home-filled /></el-icon>
                        <span>首页</span>
                    </el-menu-item>
                    <el-sub-menu index="/news">
                        <template #title>
                            <el-icon><message /></el-icon>新闻管理
                        </template>
                        <el-menu-item index="/news/addnews">
                            <span>创建新闻</span>
                        </el-menu-item>
                        <el-menu-item index="/news/newslist">
                            <span>新闻列表</span>
                        </el-menu-item>
                    </el-sub-menu>
                </el-menu>
            </el-scrollbar>
        </el-aside>

        <el-container>
            <el-header>
                <div>新闻管理系统</div>
                <div>欢迎回来</div>
            </el-header>

            <el-main>
                <el-scrollbar>
                    <router-view></router-view>
                </el-scrollbar>
            </el-main>
        </el-container>
    </el-container>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { Menu as IconMenu, Message, Setting, HomeFilled } from "@element-plus/icons-vue";
import {useRoute} from "vue-router"

const route = useRoute()
console.log(route.fullPath);

const item = {
    date: "2016-05-02",
    name: "Tom",
    address: "No. 189, Grove St, Los Angeles",
};
const tableData = ref(Array.from({ length: 20 }).fill(item));
</script>

<style scoped>
/* .layout-container-demo .el-header {
    position: relative;
    background-color: var(--el-color-primary-light-7);
    color: var(--el-text-color-primary);
}
.layout-container-demo .el-aside {
    color: var(--el-text-color-primary);
    background: var(--el-color-primary-light-8);
}
.layout-container-demo .el-menu {
    border-right: none;
}
.layout-container-demo .el-main {
    padding: 0;
}
.layout-container-demo .toolbar {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    right: 20px;
} */

.el-header{
    background-color: lightcoral;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
</style>
