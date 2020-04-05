importScripts('/_nuxt/workbox.4c4f5ca6.js')

workbox.precaching.precacheAndRoute([
  {
    "url": "/_nuxt/17cf321c26980e18a79e.js",
    "revision": "c61e702426426cea27617fd7a4354f8b"
  },
  {
    "url": "/_nuxt/1f7941f18d8856458b52.js",
    "revision": "448cafe9882c25f415018f0f546586c4"
  },
  {
    "url": "/_nuxt/211c5e7f908cbd89a55f.js",
    "revision": "ad97ccb209af5bddd309968bf1324796"
  },
  {
    "url": "/_nuxt/2f34f34e1fa2006c6548.js",
    "revision": "b985f4cd50fbf0836a954d5d460950e0"
  },
  {
    "url": "/_nuxt/447ccdd059b854aac7df.js",
    "revision": "01832afa5fb8b49d59873c1d880e78bf"
  },
  {
    "url": "/_nuxt/4ab26126ab83948eb8d4.js",
    "revision": "32ced72a8821a35c11188cee497d4bd4"
  },
  {
    "url": "/_nuxt/51faa11917ac1902f322.js",
    "revision": "d04901e632ecbcf6cd25705edfda8f61"
  },
  {
    "url": "/_nuxt/5db4d690e128ea6fd6ee.js",
    "revision": "3ea65e935027599994b736ff86f74b32"
  },
  {
    "url": "/_nuxt/62965324a0b40cbc406e.js",
    "revision": "44ca844b0879aa693f5085ea46fc77be"
  },
  {
    "url": "/_nuxt/7611bf68cc904a236b65.js",
    "revision": "c35d461599b3dd5262340db42618edec"
  },
  {
    "url": "/_nuxt/80920471d14f2a588e18.js",
    "revision": "9267317faad66c7c3bde1a7b0f888bd8"
  },
  {
    "url": "/_nuxt/a26e1e384890347aa4c9.js",
    "revision": "47ee19ea007592df798e2972264d0e2d"
  },
  {
    "url": "/_nuxt/a4a12d173fdd836de455.js",
    "revision": "d86ddc88d01916391ce1cf942f6a1d2e"
  },
  {
    "url": "/_nuxt/a9ec62cf95833a5cc4ca.js",
    "revision": "2405e1874585b0e1aac3ea88eae1d5c8"
  },
  {
    "url": "/_nuxt/b2a5cc1eaa5cfa64d408.js",
    "revision": "450800567632b1c29a20f860ae69c8ef"
  },
  {
    "url": "/_nuxt/b568fa55004011a744c8.js",
    "revision": "cae4092e4e5d4b08e3909e0a9810bfaa"
  },
  {
    "url": "/_nuxt/b691cc968c598945ab77.js",
    "revision": "1d500c5da6797847e9ded2cb1c0574af"
  },
  {
    "url": "/_nuxt/c7c22cb96223d3235914.js",
    "revision": "c12bece64e9356223128d95a4ef10422"
  },
  {
    "url": "/_nuxt/ca547c8911a45ab98ba3.js",
    "revision": "9e70dde5173365ec71aae8f48e297e4e"
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
