import axios from 'axios'

let instance = axios.create({
  baseURL: process.env.BASE_URL
})

export default function ({ $axios, store }) {
  $axios.onRequest( (config) => {
    if (store.state.token) {
      config.headers.common['Authorization'] = `JWT ${store.state.token}`
    }
  })
 }
