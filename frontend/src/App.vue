<template>
  <v-app>
    <v-app-bar :elevation="0" color="#121212 " class="mx-0" style="background: rgba(18, 18, 18, 0.84)">
      <v-container>
        <div class="d-flex align-center justify-space-between my-2">
          <!-- 홈 버튼 -->
          
          <v-btn link :to="{ name: 'MovieView' }" color="#121212">
            <div class="d-flex align-center">
              <v-img width="48" cover src="https://i.postimg.cc/RhgGhzTn/MM-logo-removebg.png" border="0" alt="MM-Icon"></v-img>
            </div>
          </v-btn>
        
          <v-spacer></v-spacer>
          
          <!-- nav bar 옵션: 안 보여서 일단 주석 처리 -->
          <!-- <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon> -->

          <!-- 로그인 된 상태 -->
          <template v-if="store.isLogIn">
            <v-spacer></v-spacer>
            <v-row align="right">
              <v-col class="d-flex align-center">
                <!-- 검색창 -->
                <v-container>
                  <div class="input-group my-3">
                    <input
                      type="text"
                      label="Search"
                      v-model.trim="searchWord"
                      class="form-control violet-background"
                      placeholder="Enter any movie titles, genres, or actors you're looking for!"
                      aria-label="Recipient's username"
                      aria-describedby="button-addon2"
                      outlined
                      style="width: 25% max-width"
                      font-size="16"
                      @keyup.enter="search"
                      >
                    <!--vuetify의 v-text-field 사용-->
                    <!-- <v-text-field
                      v-model.trim="searchWord"
                      label="Search"
                      placeholder="Enter any movie titles, genres, or actors you're looking for!"
                      outlined
                      class="form-control"
                      style="width: 25% max-width"
                      @keyup.enter="search"
                    ></v-text-field> -->
                    <button @click="search" class="btn btn-outline-secondary" type="button" id="button-addon2" style="background-color: #A44CD3;">Search</button>
                  </div>
                </v-container>
                
                <!-- 다크 모드 변경 -->
                <div class="d-flex align-center">
                  <v-btn :elevation="2" @click="toggleTheme" v-if="!theme.global.current.value.dark" outlined style="border-width: 0.5px; border-color: dark;">
                    <div style="font-size: 8px;">Mode Change<br>(Dark  Mode)</div>
                  </v-btn>
                  <v-btn :elevation="2" @click="toggleTheme" v-if="theme.global.current.value.dark" outlined style="border-width: 0.5px; border-color: dark;">
                    <div style="font-size: 8px;">Mode Change<br>(Light Mode)</div>
                  </v-btn>
                </div>
                <v-spacer></v-spacer>
                  <!-- 로그아웃 버튼 -->
                <div class="d-flex align-center">
                  <v-btn @click="handleLogout"  outlined style="background-color: #a44cd3; border-width: 2px; border-color: dark; border-radius: 8px;" text>Logout</v-btn>
                </div>
                <div class="d-flex align-center">
                  <v-btn @click="toMyPage">
                    <v-avatar color="surface-variant" size="40" image="/src/assets/profile_default.png">
                      <v-img src="/src/assets/profile_default.png"></v-img>
                    </v-avatar>
                  </v-btn>
                </div>
              </v-col>
            </v-row>
          </template>

          <!-- 로그인 안 했을 때 보이는 거 -->
          <template v-else>
            <v-spacer></v-spacer>
            <v-row align="right">
              <v-col class="d-flex align-center">
                <!-- 다크 모드 변경 -->
                <div class="d-flex align-center">
                  <v-btn @click="toggleTheme" v-if="!theme.global.current.value.dark">
                    <div style="font-size: 8px;">Mode Change<br>(Dark  Mode)</div>
                  </v-btn>
                  <v-btn @click="toggleTheme" v-if="theme.global.current.value.dark">
                    <div style="font-size: 8px;">Mode Change<br>(Light Mode)</div>
                  </v-btn>
                  <!-- 회원가입, 로그인 이동 라우터 -->
                  <v-btn @click="goToSignUpPage">SignUp
                    <!-- <router-link :to="{ name: 'SignUpView' }">회원가입</router-link> -->
                  </v-btn> | 
                  <v-btn @click="goToLogInPage">Login
                    <!-- <router-link :to="{ name: 'LogInView' }">로그인</router-link> -->
                  </v-btn>
                </div>
              </v-col>
            </v-row>
          </template>
          
        </div>
      </v-container>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
  <!-- <RouterView /> -->
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import { useTheme } from 'vuetify'

const store = useCounterStore()
const router = useRouter()
const theme = useTheme()

const handleLogout = () => {
  store.logOut()
  // 로그아웃 후 로그인되지 않은 상태에서 로그인 페이지로 이동
  router.push({ name: 'LogInView' })
}

function toggleTheme () {
  const newTheme = theme.global.current.value.dark? 'light': 'dark'
  theme.global.name.value = newTheme
  localStorage.setItem('themePreference', newTheme)
}

// themePreference에 저장해서 페이지 새로고침 시 현재 모드 유지
const storedTheme = localStorage.getItem('themePreference')
if (storedTheme) {
  theme.global.name.value = storedTheme
}

const toMyPage = () => {
  // router.push({ name: 'MyPageView' })
  router.push({ name: 'MyPageView', params: { username: store.username0 }})
}

const goToSignUpPage = () => {
  router.push({ name: 'SignUpView'})
}

const goToLogInPage = () => {
  router.push({ name: 'LogInView'})
}

const searchWord = ref('')
const search = (() => {
  router.push({ name: 'SearchView', params: { word: searchWord.value }})
  searchWord.value = ''
})

</script>

<style>
@import './assets/styles/main.css';

.navbar {
  padding: 5px;
}
v-img {
  height: 50px;
}
.dark-background {
    background-color: #b3b3b3; /* color 수정 */
    color: #444444; /* 글자색 조정 */
    }
.mc-3 {
  color: #FBBEDE
}
</style>