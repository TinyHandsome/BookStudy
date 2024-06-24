<template>
    <div>
        NewsList
        <el-carousel :interval="4000" type="card" height="200px">
            <el-carousel-item v-for="item in 6" :key="item">
                <h3 text="2xl" justify="center">{{ item }}</h3>
            </el-carousel-item>
        </el-carousel>

        <el-row
            :gutter="20"
            style="
                align-items: center;
                justify-content: space-between;
                background-color: lightgray;
            "
        >
            <el-col :span="8">
                <div class="grid-content ep-bg-purple">个人介绍</div>
            </el-col>
            <el-col :span="8">
                <div class="grid-content ep-bg-purple-light">公司介绍</div>
            </el-col>
            <el-col :span="8">
                <div class="grid-content ep-bg-purple">公司产品</div>
            </el-col>
        </el-row>

        <el-table :data="store.list" style="width: 100%">
            <el-table-column label="标题" width="180">
                <template #default="scope">
                    <b style="margin-left: 10px; color: red">{{ scope.row.title }}</b>
                </template>
            </el-table-column>
            <el-table-column prop="category" label="分类" width="180" />
            <el-table-column prop="content" label="内容" />
            <el-table-column>
                <template #default="scope">
                    <div>
                        <el-button type="warning" round>编辑</el-button>
                        <el-button type="danger" round>删除</el-button>
                    </div>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script setup>
import useNewsStore from "../store/news";

const store = useNewsStore();
console.log(store.list);
</script>

<style scoped>
.el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    text-align: center;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}
</style>
