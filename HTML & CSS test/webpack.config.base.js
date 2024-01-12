const path = require('path');

const JS = {
    test: /\.js$/,
    exclude: /(node_modules|bower_components)/,
    use: "babel-loader"
};

const FONTS = {
    test: /fonts\/.*\.(ttf|eot|otf|svg|woff|woff2)$/,
    use: {
        loader: "file-loader",
        options: {
            name: "[name].[ext]",
        },
    },
};

// const IMAGES = {
//     test: /images\/.*\.(svg|jpe?g|png|gif)$/,
//     use: [
//         {
//             loader: 'file-loader',
//             options: {
//                 name: '[name].[ext]',
//             }
//         },
//         {
//             loader: 'image-webpack-loader',
//             options: {
//                 mozjpeg: {
//                     progressive: true,
//                     quality: 80
//                 },
//                 optipng: {
//                     enabled: false,
//                 },
//                 pngquant: {
//                     quality: '65-90',
//                     speed: 4
//                 },
//                 gifsicle: {
//                     interlaced: false,
//                 },
//             }
//         }
//     ],
// };

const PATH = {
    entry: path.join(__dirname, "src", "entry.js"),
    build: path.join(__dirname, "dist", "build")
};

module.exports = {
    mode: "none",
    context: __dirname,
    entry: ["babel-polyfill", PATH.entry],
    output: {
        filename: "build.js",
        path: PATH.build,
    },
    module: {
        rules: [
            JS,
            FONTS,
            // IMAGES
        ]
    },
    resolve: {
        extensions: ['.js'],
        modules: [path.resolve(__dirname, 'src', 'js'), 'node_modules']
    }
};
