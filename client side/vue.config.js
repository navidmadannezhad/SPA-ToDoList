path = require('path')

module.exports = {
    configureWebpack: {
        resolve:{
            alias:{
                '@': path.resolve(__dirname, 'public/'),
                'mixins': path.resolve(__dirname, 'src/mixins.js'),
            }
        }
    }
}