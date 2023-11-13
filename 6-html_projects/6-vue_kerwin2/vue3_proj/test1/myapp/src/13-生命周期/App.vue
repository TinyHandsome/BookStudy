<template>
    <div id="main" style="width: 600px; height: 400px;"></div>
    <div>{{ title }}</div>
</template>

<script>
// 导出了一堆方法
import * as echarts from "echarts";
export default {
    data() {
        return {
            title: "111",
        };
    },
    mounted() {
        var myChart = echarts.init(document.getElementById("main"));
        myChart.setOption({
            title: {
                text: "ECharts 入门示例",
            },
            tooltip: {},
            xAxis: {
                data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
            },
            yAxis: {},
            series: [
                {
                    name: "销量",
                    type: "bar",
                    data: [5, 20, 36, 10, 10, 20],
                },
            ],
        });
    },
};
</script> 

<style scoped></style>
