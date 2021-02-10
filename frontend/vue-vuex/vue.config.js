// config/index.js
// module.exports = {
//   // ...
//   build: {
//     assetsPublicPath: "/",
//     assetsSubDirectory: "assets",
//   },
// };

module.exports = {
  devServer: {
    proxy: "http://localhost:8000/",
  },
};
