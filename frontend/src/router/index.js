import { createRouter, createWebHistory } from 'vue-router'
import MovieView from '@/views/MovieView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ProfilesAddView from '@/views/ProfilesAddView.vue'
import { useCounterStore } from '@/stores/counter'
import MovieDetailView from '@/views/MovieDetail.vue'
import MyPageView from '@/views/MyPageView.vue'
import SearchView from '@/views/SearchView.vue'
import PeopleView from '@/views/PeopleView.vue'
import GenreView from '@/views/GenreView.vue'
import StartView from '@/views/StartView.vue' 

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MovieView',
      component: MovieView,
      // 로그인이 필요한 사이트임을 표시(아래에 RouteGuard도 추가)
      meta: { requiresAuth: true },
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/movie/:id',
      name: 'MovieDetailView',
      component: MovieDetailView
    },
    {
      path: '/profiles/add',
      name: 'ProfilesAddView',
      component: ProfilesAddView
    },
    {
      path: '/profiles/:username',
      name: 'MyPageView',
      component: MyPageView
    },
    {
      path: '/search/:word',
      name: 'SearchView',
      component: SearchView
    },
    {
      path: '/people/:id',
      name: 'PeopleView',
      component: PeopleView
    },
    {
      path: '/genre/:genre',
      name: 'GenreView',
      component: GenreView
    },
    {
      path: '/firstpick',
      name: 'StartView',
      component: StartView
    },
  ]
})

router.beforeEach((to, from) => {
  const store = useCounterStore()
  // 로그인 하지 않은 유저는 메인 페이지 접근 제한
  if (to.name === 'MovieView' && !store.isLogIn) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  // 로그인 한 사용자는 로그인 페이지 & 회원가입 페이지 접근 제한
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogIn)) {
    // window.alert('이미 로그인 되어있습니다.')
    return { name: 'MovieView' }
  }
})

export default router
