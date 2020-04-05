importScripts('/_nuxt/workbox.4c4f5ca6.js')

workbox.precaching.precacheAndRoute([
  {
    "url": "/_nuxt/069f007b615de8e2f9df.js",
    "revision": "e17c2e800e68990c87c2acea50b1e307"
  },
  {
    "url": "/_nuxt/06ad6de17b8ff1c1c911.js",
    "revision": "040db533f5f07882f33fc000e17d7f76"
  },
  {
    "url": "/_nuxt/4dc15dc981a8d473ad75.js",
    "revision": "92f5b75eb2eb80390abcda8197cf537b"
  },
  {
    "url": "/_nuxt/506cb479b66d8f0f3c72.js",
    "revision": "f54e63803c639f67dc385cb3a249e069"
  },
  {
    "url": "/_nuxt/6017c32546ed3e8bda6b.js",
    "revision": "0dec31e846aceccef81f5083d1916d6a"
  },
  {
    "url": "/_nuxt/6ca973ca5e17b32bb5fd.js",
    "revision": "1f8505358f02a6bcfabe9d2bb586df97"
  },
  {
    "url": "/_nuxt/70cb4c921157efc76603.js",
    "revision": "c8da1ae4f367bcef590ced0c9791624e"
  },
  {
    "url": "/_nuxt/79ad031aad505e75050d.js",
    "revision": "02476be4041a94ed9f6cdc1b6ffd4105"
  },
  {
    "url": "/_nuxt/7f266021b30ad2ffec17.js",
    "revision": "3e8462e952fe234eb9ef5a361c69679e"
  },
  {
    "url": "/_nuxt/9d654d71334c821e5ce0.js",
    "revision": "3edc4b0423fd51140f47b24f7efca34b"
  },
  {
    "url": "/_nuxt/ab871863149ea5851344.js",
    "revision": "db488813d09b6a727a5e8af48c3a70c4"
  },
  {
    "url": "/_nuxt/cf282bafdce838010459.js",
    "revision": "b5a13d84eb30ded45310da70e8b847e0"
  },
  {
    "url": "/_nuxt/d1da3fe100da569289db.js",
    "revision": "c2fd2c44195d62fe22689dea43cc07f9"
  },
  {
    "url": "/_nuxt/d5408959a9f81ad4fa0e.js",
    "revision": "0f1760c808554c01c0e1841a50852cbe"
  },
  {
    "url": "/_nuxt/e4f6b93b9b80b2238182.js",
    "revision": "3d3f9c4e63b9cd4e7913fd4f10a810a4"
  },
  {
    "url": "/_nuxt/f96c794e50f7757dc80b.js",
    "revision": "ac3faa56567ecefff20be7616307569f"
  },
  {
    "url": "/_nuxt/fee40e88f6133bbdb364.js",
    "revision": "0d18904460ae55c4074643d03d783072"
  },
  {
    "url": "/_nuxt/ffec9a321b89c5e4a2bf.js",
    "revision": "c0ba07ec5efc7db63df964d72052fcce"
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
