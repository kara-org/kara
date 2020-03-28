const env = require('dotenv').config();
const nodeExternals = require('webpack-node-externals');

export default {
  mode: 'universal',
  /*
   ** Headers of the page
   */
  head: {
    title:
      'Kara: Mudar o mundo uma doação por vez' || process.env.npm_package_name,
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: ['~assets/styles/main.scss'],

  styleResources: {
    scss: ['~assets/styles/main.scss']
  },
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [
    { src: '~/plugins/vee-validate' },
    { src: '~/plugins/via-cep' },
    { src: '~/plugins/axios' },
    { src: '~/plugins/services' }
    // { src: '~/plugins/vue-videobg' },
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://buefy.github.io/#/documentation
    'nuxt-buefy',
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    ['nuxt-sass-resources-loader', './assets/styles/main.scss'],
    '@nuxtjs/style-resources',
    [
      'nuxt-parse',
      {
        appId: 'ElfuZaaNpkOuF9DvMrAnfPxOypoxH1HT72jxLmTG',
        javascriptKey: 'KZqP3vpzqc1E6nefOqeE6h9HZ9s92iiRSJGhM147',
        serverUrl: 'https://kara.back4app.io'
      }
    ]
  ],
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    baseURL: process.env.BASE_URL || 'http://localhost:8000/api'
  },

  /*
   ** Build configuration
   */
  env: env.parsed,

  build: {
    /*
     ** You can extend webpack config here
     */
    extend(config, { isServer }) {
      // const vueLoader = config.module.rules.find((rule) => rule.loader === 'vue-loader')
      // vueLoader.query.loaders.scss = 'vue-style-loader!css-loader!sass-loader?' + JSON.stringify({ includePaths: [path.resolve(__dirname), 'node_modules'] })

      if (isServer) {
        config.externals = [
          nodeExternals({
            whitelist: [/\.(?!(?:js|json)$).{1,5}$/i, /^vue-videobg/]
          })
        ];
      }
    }
  }
};
