import axios from 'axios'

let instance = axios.create({
  baseURL: 'http://localhost:8000/api'
})

export default function ({ $axios, store }) {
  $axios.onRequest( (config) => {
    if (store.state.token) {
      config.headers.common['Authorization'] = `JWT ${store.state.token}`
    }
  })
 }
