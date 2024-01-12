const webpack = require("webpack");
const merge = require("webpack-merge");
const baseConfig = require("./webpack.config.base");

const CleanWebpackPlugin = require("clean-webpack-plugin");
const UglifyJsPlugin = require("uglifyjs-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const cssnano = require("cssnano");

const PLUGINS = [
    new CleanWebpackPlugin("dist/build"),
    new MiniCssExtractPlugin({
        filename: "build.css"
    }),
    new webpack.ProvidePlugin({
        $: 'jquery',
        jQuery: 'jquery'
    })
];

const SCSS = {
    test: /\.scss$/,
    use: [
        MiniCssExtractPlugin.loader,
        "css-loader",
        {
            loader: "postcss-loader",
            options: {
                plugins: () => ([
                    require("autoprefixer")
                ]),
            },
        },
        {
            loader: "resolve-url-loader"
        },
        {
            loader: "sass-loader",
            options: {
                sourceMap: true
            }
        }
    ]
};

module.exports = merge(baseConfig, {
    mode: "production",
    module: {
        rules: [
            SCSS
        ]
    },
    optimization: {
        minimizer: [
            new UglifyJsPlugin({
                cache: true,
                parallel: true,
            }),
            new OptimizeCSSAssetsPlugin({
                cssProcessor: cssnano,
                cssProcessorOptions: {
                    discardComments: {
                        removeAll: true
                    }
                },
                canPrint: false
            })
        ]
    },
    devtool: process.env.sourcemap ? "eval-source-map" : "none",
    plugins: PLUGINS
});
