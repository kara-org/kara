importScripts('/_nuxt/workbox.4c4f5ca6.js')

workbox.precaching.precacheAndRoute([
  {
    "url": "/_nuxt/097af8f4cc4c9755fd2f.js",
    "revision": "cd693c9faccd3b4f675889f58a44fb4b"
  },
  {
    "url": "/_nuxt/14fedb1e3767d390c4de.js",
    "revision": "ab588d83fe535cdddb15f33faa12b17d"
  },
  {
    "url": "/_nuxt/1781fdaaf1a4a4b7d9bd.js",
    "revision": "2dcb924740aa844a0eeedb532a225da2"
  },
  {
    "url": "/_nuxt/19b17d78eee575ca8118.js",
    "revision": "a3af756b437518f53e1753aceac54f9c"
  },
  {
    "url": "/_nuxt/20a6d58ef8affddd13e8.js",
    "revision": "c65f25ee4e39bc7aab709b2d6f17b162"
  },
  {
    "url": "/_nuxt/21a3afd502fe3afec376.js",
    "revision": "d6c92ec655f6cd8c2a252bef5354e0c9"
  },
  {
    "url": "/_nuxt/317c7f456ccd7dabe241.js",
    "revision": "65403034c7d2221cbfdabb4195ab3072"
  },
  {
    "url": "/_nuxt/3ca9c5e1db5930be1fc2.js",
    "revision": "d572d761a317783b00af21b9a26ba512"
  },
  {
    "url": "/_nuxt/4124d5da036bc632cc3d.js",
    "revision": "b331df780a9b790392976c2814fb04ee"
  },
  {
    "url": "/_nuxt/4aae4cb04d4dfa5c168b.js",
    "revision": "1e6a246cff41741b02de6eb1f0a66b6b"
  },
  {
    "url": "/_nuxt/4c5b1dbfab428d8acf3d.js",
    "revision": "ae7d5c559b310b33f33cbf2ac7fe41df"
  },
  {
    "url": "/_nuxt/60745c25508f135ed641.js",
    "revision": "7cdd7d41627dbc802cdcc3f131d5c2e6"
  },
  {
    "url": "/_nuxt/6a9b287d384bf634375f.js",
    "revision": "bc686efe974e428c97c98d025796a25e"
  },
  {
    "url": "/_nuxt/9e78cb60d041e07f856a.js",
    "revision": "7b059d9e0e1cba95991ca361a2c9de94"
  },
  {
    "url": "/_nuxt/c5e42f4f56f7ded39bd5.js",
    "revision": "bf291e7f28c01532fbe10de3c04a3bac"
  },
  {
    "url": "/_nuxt/c93c8b911990d8b793de.js",
    "revision": "60552307fb00fe33022602da7338df7e"
  },
  {
    "url": "/_nuxt/cbec71d91233af21b976.js",
    "revision": "337f21e0eb72c72a677f779a1c10f472"
  },
  {
    "url": "/_nuxt/d5b6a372320406e0a361.js",
    "revision": "0160a524d5be8c9d52d1d6c26635a108"
  }
], {
  "cacheId": "kara-client",
  "directoryIndex": "/",
  "cleanUrls": false
})

workbox.clientsClaim()
workbox.skipWaiting()

workbox.routing.registerRoute(new RegExp('/_nuxt/.*'), workbox.strategies.cacheFirst({}), 'GET')

workbox.routing.registerRoute(new RegExp('/.*'), workbox.strategies.networkFirst({}), 'GET')
