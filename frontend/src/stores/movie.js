import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'

export const useMovieStore = defineStore('movie', () => {
  const store = useCounterStore()
  const router = useRouter()

  const topRated = ref([])
  // axios({
  //   method: 'get',
  //   url: `${store.API_URL}/api/v1/movies/top_rated/`,
  //   headers: {
  //     Authorization: `Token ${store.token}`
  //   }
  // }).then((res) => {
  //   topRated.value = res.data
  //   router.push({ name: 'LogInView' })
  // }).catch((err) =>{
  //   console.log(err)
  // })

  const getTopRated = (() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/api/v1/movies/top_rated/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    }).then((res) => {
      topRated.value = res.data
    }).catch((err) =>{
      console.log(err)
    })
  })

  const upcoming = ref([])
  // axios({
  //   method: 'get',
  //   url: `${store.API_URL}/api/v1/movies/upcoming/`,
  //   headers: {
  //     Authorization: `Token ${store.token}`
  //   }
  // }).then((res) => {
  //   upcoming.value = res.data
  //   router.push({ name: 'LogInView' })
  // }).catch((err) =>{
  //   console.log(err)
  // })
  const getUpcoming = (() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/api/v1/movies/upcoming/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    }).then((res) => {
      upcoming.value = res.data
    }).catch((err) =>{
      console.log(err)
    })
  })
  

  const nowPlaying = ref([])
  // axios({
  //   method: 'get',
  //   url: `${store.API_URL}/api/v1/movies/now_playing/`,
  //   headers: {
  //     Authorization: `Token ${store.token}`
  //   }
  // }).then((res) => {
  //   nowPlaying.value = res.data
  //   console.log(nowPlaying)
  // }).catch((err) => {
  //   console.log(err)
  // })
  const getNowPlaying = (() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/api/v1/movies/now_playing/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    }).then((res) => {
      nowPlaying.value = res.data
    }).catch((err) => {
      console.log(err)
    })
  })
  
  

  return { topRated, upcoming, nowPlaying, getNowPlaying, getTopRated, getUpcoming }
}, { persist: true })
