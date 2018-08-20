var path = require('path')
var webpack = require('webpack')
var projectRoot = process.env.PWD; // Absolute path to the project root
// const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    entry: './static/js/App.js',
    output: {
        path: path.join(__dirname, './static/public'),
        publicPath: '/static/public/',
        filename: 'bundle.js'
    },
    // plugins: [
    //     new HtmlWebpackPlugin({
    //         title: 'ngRedux Async',
    //         template: './homepage/templates/homepage/index.html',
    //         inject: 'body'
    //     })
    // ],
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                    loaders: {
                    }
                    // other vue-loader options go here
                }
            },
            {
                test: /\.js$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            },
            {
                test: /\.html$/,
                use: [{
                    loader: 'html-loader'
                }]
            },
            {
                test: /\.(png|jpg|gif|svg)$/,
                loader: 'file-loader',
                options: {
                    name: '[name].[ext]?[hash]'
                }
            }
        ]
    },
    performance: {
        hints: false
    },
    devtool: '#eval-source-map'
}


if (process.env.NODE_ENV === 'production')
{
    module.exports.devtool = '#source-map'
    
    module.exports.plugins = (module.exports.plugins || []).concat([
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: '"production"'
            }
        }),
        new webpack.optimize.UglifyJsPlugin({
            sourceMap: true,
            compress: {
                warnings: false
            }
        }),
        new webpack.LoaderOptionsPlugin({
            minimize: true
        })
    ])
}