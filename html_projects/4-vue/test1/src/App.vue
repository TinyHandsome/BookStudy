<template>
  <div>
    <tabbar></tabbar>
    <!-- 路由容器 -->
    <section>
      <router-view></router-view>
    </section>
  </div>
  <!-- <div>
    hello app --{{ myname }}
    <img src="/2.3.jpg" alt="" />
    <input type="text" v-model="mytext" />
    <button @click="handleAdd">add</button>
    <ul>
      <li v-for="data in datalist" :key="data">
        {{ data }}
      </li>
    </ul>
    <navbar myname="home" :myright="false" @event="handleEvent">
      <div>111111</div>
    </navbar>
    <sidebar v-show="isShown"></sidebar>
    <div v-hello>111111</div>
    <div v-hello>222222</div>

    <img :src="imgUrl | imgFilter" alt="" />
  </div> -->
</template>

<script>
// ES6 导出规范 --babel(ES6 ==> ES5)
import navbar from "./components/Navbar";
import sidebar from "./components/Sidebar.vue";
import Vue from "vue";
import axios from "axios";
import tabbar from "@/components/Tabbar";

// Vue.component("navbar", navbar)
Vue.directive("hello", {
  inserted(el, binding) {
    console.log(el);
    el.style.border = "1px solid black";
  },
});
Vue.filter("imgFilter", (path) => {
  return path.replace("/w.h", "") + "123123asdasd";
});

export default {
  data() {
    return {
      myname: 123,
      mytext: "haha",
      datalist: [],
      isShown: true,
      imgUrl:
        "https://gimg3.baidu.com/search/src=http%3A%2F%2Fpics7.baidu.com%2Ffeed%2F5882b2b7d0a20cf4e9e31c42285c2f3aadaf999a.jpeg%40f_auto%3Ftoken%3Db9b414420cca3ae716af86da02e57457&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=f360,240&n=0&g=0n&q=75&fmt=auto?sec=1688058000&t=71ee4a2e9ddfb8690446c5ae20a57bc7",
    };
  },
  components: {
    navbar,
    sidebar,
    tabbar,
  },
  methods: {
    handleAdd() {
      console.log(this.mytext);
      this.datalist.push(this.mytext);
    },
    handleEvent() {
      this.isShown = !this.isShown;
    },
  },
  computed: {},
  watch: {},
  mounted() {
    const config = {
      headers: {
        Authorization:
          "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3OTQ4OTM1LCJpYXQiOjE2ODc5MjAxMzUsImp0aSI6ImM2MjE4MTQ1MTAyNzQ1Mzc5N2JmMzZjNDViYjdlYWM5IiwidXNlcl9pZCI6M30.X2SzT8RN1KRZjSdMDaikETYsC6a9Sl0K76jvNfiytXc",
      },
    };
    axios
      .post(
        "http://10.80.97.74:8000/chatgpt/conversation/",
        { conversation_id: 244 },
        config
      )
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>

<style lang="scss">
* {
  margin: 0;
  padding: 0;
}
html,
body {
  height: 100%;
}

ul {
  list-style: none;
}

section {
  padding-bottom: 3.0625rem;
}
</style>
