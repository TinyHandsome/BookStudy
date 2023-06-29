const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  // 暂时关闭代码检测
  lintOnSave: false,

  // 配置反向代理
  devServer: {
    proxy: {
      "/ajax": {
        target: "https://m.maoyan.com",
        changeOrigin: true
      },

      // 凡是kerwin请求的，都会拦截之后，进行路径的替换和反向代理
      "/kerwin": {
        target: "https://m.maizuo.com",
        changeOrigin: true,
        pathRewrite: {
          "/kerwin": ''
        }
      },
    }
  }
})
