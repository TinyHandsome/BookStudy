<template>
    <el-form :model="form" label-width="120px">
        <el-form-item label="新闻标题">
            <el-input v-model="form.title" />
        </el-form-item>
        <el-form-item label="新闻分类">
            <el-select v-model="form.category" placeholder="请选择你的分类">
                <el-option label="经济" value="经济" />
                <el-option label="明星" value="明星" />
                <el-option label="科技" value="科技" />
            </el-select>
        </el-form-item>
        <el-form-item label="新闻内容">
            <el-input v-model="form.content" type="textarea" />
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onSubmit">Create</el-button>
            <el-button>Cancel</el-button>
        </el-form-item>
    </el-form>
</template>

<script setup>
import { reactive } from "vue";
import useNewsStore from "../store/news";
import { useRouter } from "vue-router";

const store = useNewsStore();
const router = useRouter()

// do not use same name with ref
const form = reactive({
    title: "",
    category: "",
    content: "",
});

const onSubmit = () => {
    console.log("submit!", form);
    store.add(form);
    router.push('/news/newslist')
};
</script>
