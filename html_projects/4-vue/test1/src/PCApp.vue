<template>
  <div>
    <el-button @click="handlePrimary" size="mini">默认按钮</el-button>
    <el-button type="primary" size="small">主要按钮</el-button>
    <el-button type="success" :plain="true">成功按钮</el-button>
    <el-button type="info" :round="true">信息按钮</el-button>
    <el-button type="warning">警告按钮</el-button>
    <el-button type="danger">危险按钮</el-button>
  </div>
</template>

<script>
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import Vue from "vue";
Vue.use(ElementUI);

export default {
  methods: {
    handlePrimary() {
      console.log("好耶");
    },
  },
};
</script>
