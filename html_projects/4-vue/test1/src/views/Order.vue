<template>
  <div>订单</div>
</template>

<script>
import axios from "axios";
export default {
  mounted() {
    axios
      .get(
        "/ajax/api/mmdb/movie/v3/list/hot.json?ct=%E7%83%9F%E5%8F%B0&ci=104&channelId=4"
      )
      .then((res) => {
        console.log(res.data);
      });
  },
};
</script>
