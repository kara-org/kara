const env = require('dotenv').config();
const nodeExternals = require('webpack-node-externals');
import axios from 'axios';

export default {
  mode: 'universal',
  /*
   ** Headers of the page
   */

  // TODO: Criar dinamicamente as rotas
  generate: {
    routes() {
      return axios
        .get('https://kara.back4app.io/classes/Ong', {
          headers: {
            'accept': 'application/json',
            'X-Parse-Application-Id': 'ElfuZaaNpkOuF9DvMrAnfPxOypoxH1HT72jxLmTG',
            'X-Parse-REST-API-Key': '92n38U9r6jitkaFn57hbUCPnMLhJ7JFVYZsaKuBv'
          }
        })
        .then(res => {
          return res.data.results
            .filter(o => o.slug != undefined)
            .map(ong => {
              return '/ong/' + ong.slug;
            });
        });
    }
  },

  head: {
    htmlAttrs: {
      lang: 'pt'
    },
    title:
      'Kara: Mudar o mundo uma doação por vez' || process.env.npm_package_name,
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      },
      {
        hid: 'og:site_name',
        property: 'og:title',
        content: 'Kara: Mudar o mundo uma doação por vez'
      },
      {
        hid: 'og:title',
        property: 'og:title',
        content: 'Kara: Mudar o mundo uma doação por vez'
      },
      {
        hid: 'og:description',
        property: 'og:description',
        content: process.env.npm_package_description || ''
      },
      { hid: 'og:type', property: 'og:type', content: 'website' },
      {
        hid: 'og:url',
        property: 'og:url',
        content: 'https://karadoacoes.com.br'
      },
      {
        hid: 'og:image',
        property: 'og:image',
        content: 'https://karadoacoes.com.br/meta_640.png'
      },
      // Twitter Card
      { hid: 'twitter:card', name: 'twitter:card', content: 'summary' },
      // { hid: 'twitter:site', name: 'twitter:site', content: 'https://karadoacoes.com.br' },
      {
        hid: 'twitter:title',
        name: 'twitter:title',
        content: 'Kara: Mudar o mundo uma doação por vez'
      },
      {
        hid: 'twitter:description',
        name: 'twitter:description',
        ontent: process.env.npm_package_description || ''
      },
      {
        hid: 'twitter:image',
        name: 'twitter:image',
        content: 'https://karadoacoes.com.br/meta_640.png'
      },
      {
        hid: 'twitter:image:alt',
        name: 'twitter:image:alt',
        content: 'NuxtJS Logo'
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
  css: [
    '~assets/styles/main.scss',
    'material-design-icons/iconfont/material-icons.css'
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
    { src: '~/plugins/services' }
    // { src: '~/plugins/vue-videobg' },
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://buefy.github.io/#/documentation
    [
      'nuxt-buefy',
      {
        materialDesignIcons: false
      }
    ],
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
    ],
    '@nuxtjs/sitemap'
    ['@netsells/nuxt-hotjar', {
      id: '1814711',
      sv: '6',
  }],
  ],

  sitemap: {
    hostname: 'https://karadoacoes.com.br/',
    exclude: ['/auth/**', '/doador/**', '/ong/**', '/carrinho', '/busca'],
    defaults: {
      changefreq: 'daily',
      priority: 1,
      lastmod: new Date()
    }
  },
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  // axios: {
  //   baseURL: process.env.BASE_URL || 'http://localhost:8000/api'
  // },

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
