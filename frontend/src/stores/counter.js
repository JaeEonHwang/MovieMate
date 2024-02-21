import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useMovieStore } from '@/stores/movie'

export const useCounterStore = defineStore('counter', () => {
  const movieStore = useMovieStore()
  const router = useRouter()
  const articles = ref([])
  // 서버 요청 주소 확인!!
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const username0 = ref('')
  // const isNewUser = ref(false)
  const isLogIn = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // 1. DRF에 movies 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        const password = password1
        logIn2({ username, password })
        // router.push({ name: 'ProfilesAddView' })
      })
      .catch((err) => {
        console.log('회원가입 실패:', err)
        // 중복된 ID 가입 시
        if (err.response && err.response.status === 400) {
          const errorData = err.response.data
          console.log(errorData)
          // 중복된 ID로 가입 시
          if (errorData.username[0] === 'A user with that username already exists.') {
            alert('이미 사용중인 아이디입니다. 다른 ID를 사용해주세요.')
            router.push({ name: 'SignUpView' })
          } 
          // PW 불일치 시 => ticket 발행(우선순위 low로 두기)
          // else if (errorData.non_field_errors[0] === "The two password fields didn't match.") {
          //   alert("비밀번호가 일치하지 않습니다. 다시 확인해 주세요.")
          // }
          else {
            console.log(err)
          }
        }
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload
    const store = useCounterStore()
    
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log('로그인이 완료되었습니다.')
        token.value = res.data.key
        username0.value = username
        console.log(username0.value)
        movieStore.getUpcoming()
        movieStore.getNowPlaying()
        axios({
          method: 'get',
          url: `${store.API_URL}/api/v1/movies/top_rated/`,
          headers: {
            Authorization: `Token ${store.token}`
          }
        }).then((res) => {
          movieStore.topRated = res.data
          router.push({ name: 'MovieView' })
        }).catch((err) =>{
          console.log(err)
        })
      })
      .catch((err) => {
        console.log('로그인 에러:', err)
      })
  }
  const logIn2 = function (payload) {
    const { username, password } = payload
    const store = useCounterStore()
    
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log('로그인이 완료되었습니다.')
        token.value = res.data.key
        username0.value = username
        console.log(username0.value)
        movieStore.getUpcoming()
        movieStore.getNowPlaying()
        router.push({ name: 'StartView' })
        axios({
          method: 'get',
          url: `${store.API_URL}/api/v1/movies/top_rated/`,
          headers: {
            Authorization: `Token ${store.token}`
          }
        }).then((res) => {
          movieStore.topRated = res.data
          // router.push({ name: 'MovieView' })
        }).catch((err) =>{
          console.log(err)
        })
      })
      .catch((err) => {
        console.log('로그인 에러:', err)
      })
  }
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'LogInView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  return { 
    articles,
    API_URL,
    getArticles,
    signUp,
    logIn,
    token,
    isLogIn,
    logOut,
    username0,
    logIn2,
  }
}, { persist: true })
