const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyPlugin = require('copy-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = {
    // 配置环境
    mode: 'development',
    // 帮助我们在开发环境调试代码，去掉黄色警告
    devtool: 'source-map',

    // 配置入口
    entry: {
        'js/app': './src/app.js'
    },
    // 配置出口
    output: {
        path: path.join(__dirname, './dist'),
        filename: '[name].js'
    },

    module: {
        rules: [
            {
                test: /\.art$/,
                use: {
                    loader: 'art-template-loader',
                    options: {
                        escape: false
                    }
                }
            },
            {
                test: /\.css$/,
                loaders: ['style-loader', 'css-loader']
            },
            {
                test: /\.(png|jpg|gif)$/,
                use: {
                    loader: 'url-loader',
                    options: {
                        limit: 8192
                    }
                }
            }
        ]
    },
    // 配置插件
    plugins: [
        // build的时候复制index.html
        new HtmlWebpackPlugin({
            template: path.join(__dirname, './public/index.html'),
            filename: 'index.html',
            inject: true
        }),
        // build的时候复制ico
        new CopyPlugin([
            {
                from: './public/*.ico',
                to: path.join(__dirname, './dist/favicon.ico'),
                context: path.join(__dirname)
            },
            {
                from: './public/libs',
                to: path.join(__dirname, './dist/libs')
            }
        ]),
        // 每次build的时候删除dist的内容
        new CleanWebpackPlugin()
    ],
    // 配置server
    devServer: {
        contentBase: path.join(__dirname, './dist'),
        compress: true,
        port: 8080,
        proxy: {
            "/api": {
                target: "http://localhost:3000"
            }
        },
    }
}