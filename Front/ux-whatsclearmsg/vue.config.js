const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

/* vue.config.js
module.exports = {
  devServer: {
    proxy: 'http://localhost:5000', // Redirige todas las solicitudes a este puerto
  }
}
  */
