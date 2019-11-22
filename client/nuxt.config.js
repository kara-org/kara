const env = require('dotenv').config();
const nodeExternals = require('webpack-node-externals');

export default {
  mode: 'universal',
  /*
  ** Headers of the page
  */
  head: {
    title: 'Kara: Mudar o mundo uma doação por vez' || process.env.npm_package_name,
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },
  /*
  ** Global CSS
  */
  css: [
    '~assets/styles/main.scss'
  ],

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
    { src: '~/plugins/services' },
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
    '@nuxtjs/auth',
    ['nuxt-sass-resources-loader', './assets/styles/main.scss'],
    '@nuxtjs/style-resources'
  ],
  /*
  ** Axios module configuration
  ** See https://axios.nuxtjs.org/options
  */
  axios: {
    baseURL: process.env.BASE_URL || 'http://localhost:8000/api',
  },

  auth: {
    redirect: {
      login: '/auth/login',
      logout: '/',
      callback: '/auth/login',
      home: '/'
    },
    strategies: {
      local: {
        endpoints: {
          login: { url: 'login/', method: 'post', propertyName: 'token' },
          logout: false,
          user: { url: 'auth/usuario/', method: 'get', propertyName: 'data' },
        },
        tokenRequired: true,
        tokenType: 'JWT '
      }
    },
    plugins: [ '~/plugins/auth.js' ],
    watchLoggedIn: true,
    rewriteRedirects: true
  },
  /*
  ** Build configuration
  */
  env: env.parsed,

  build: {
    /*
    ** You can extend webpack config here
    */
    extend(config,  { isServer }) {
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
