<template>
  <v-card>
    <v-tabs v-model="tab" color="#FBBEDE" align-tabs="left" style="margin-left: 16px;">
      <v-tab :value="1">영화</v-tab>
      <v-tab :value="2">감독 및 배우</v-tab>
      <v-tab :value="3">장르</v-tab>
    </v-tabs>

    <v-window v-model="tab">
      <v-window-item :value="1">
        <template v-if="searchMovies">
          <v-container fluid>
            <v-row>
              <v-col>
                <div class="row row-cols-2 row-cols-md-4 row-cols-lg-6 g-4">
                  <template v-for="movie in searchMovies">
                    <!-- <SearchViewMovie :movie="movie" /> -->
                    <SearchViewMovie v-if="movie.images.length > 0 && movie.images[0].type == 1" :movie="movie" />
                  </template>
                </div>
              </v-col>
            </v-row>
          </v-container>
        </template>
      </v-window-item>

      <v-window-item :value="2">
        <template v-if="searchPeople">
          <v-container fluid>
            <v-row>
              <v-col>
                <div class="row row-cols-2 row-cols-md-4 row-cols-lg-6 g-4">
                  <SearchViewPeople v-for="person in searchPeople" :person="person" />
                </div>
              </v-col>
            </v-row>
          </v-container>
        </template>
      </v-window-item>

      <v-window-item :value="3">
        <template v-if="searchGenres">
          <v-container fluid>
            <v-row>
              <v-col>
                <div class="row row-cols-2 row-cols-md-4 row-cols-lg-6 g-4">
                  <template v-for="movie in searchGenres">
                    <!-- <SearchViewGenres :movie="movie" /> -->
                    <SearchViewGenres v-if="movie.images.length > 0 && movie.images[0].type == 1" :movie="movie" />
                  </template>
                </div>
              </v-col>
            </v-row>
          </v-container>
        </template>
      </v-window-item>
    </v-window>
  </v-card>
  
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue'
import { useRoute, onBeforeRouteUpdate, useRouter, routerKey } from 'vue-router'
import SearchViewMovie from '@/components/SearchViewMovie.vue'
import { useCounterStore } from '@/stores/counter'
import SearchViewPeople from '@/components/SearchViewPeople.vue'
import SearchViewGenres from '@/components/SearchViewGenres.vue'
import MovieDetail from './MovieDetail.vue';


const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const searchMovies = ref([])
const searchPeople = ref([])
const searchGenres = ref([])
const searchKeywords = ref([])
const searchWord1 = ref('')
const tab = ref(null)
const movieId = ref('')

axios({
  method: 'get',
  url: `${store.API_URL}/search/${route.params.word}/`,
  headers: {
    Authorization: `Token ${store.token}`,
  }
}).then((res) => {
  console.log('검색 완료')
  console.log(res.data)
  searchMovies.value = res.data.movies
  searchPeople.value = res.data.people
  searchGenres.value = res.data.genres
  console.log(res.data.genres)
}).catch((err) => {
  console.log(err)
  // window.alert(`No related words with '${ route.params.word }''`)
})

// axios({
//   method: 'get',
//   url: `${store.API_URL}/api/v1/genre/${route.params.word}/`,
//   headers: {
//     Authorization: `Token ${store.token}`,
//   }
// }).then((res) => {
//   searchGenres.value = res.data.movies
// }).catch((err) => {
//   console.log(err)
//   // window.alert(`No related genres with '${ route.params.word }''`)
// })

// const search = () => {
//   console.log(route.params.word)
//   console.log(searchWord1.value)
//   axios({
//   method: 'get',
//   url: `${store.API_URL}/search/${searchWord1.value}/`,
//   headers: {
//     Authorization: `Token ${store.token}`,
//   }
// }).then((res) => {
  
//   searchMovies.value = res.data.movies
//   searchPeople.value = res.data.people
//   searchGenres.value = res.data.genres
//   searchKeywords.value = res.data.keywords
// }).catch((err) => {
//   console.log(err)
//   // 검색 결과 없을 때 alert 띄우기
// })
// }

// 페이지 업데이트 될 때 정보 업데이트
onBeforeRouteUpdate((to, from) => {
  console.log(to.params.word)
  searchMovies.value = ''
  searchPeople.value = ''
  searchGenres.value = ''
  axios({
    method: 'get',
    url: `${store.API_URL}/search/${to.params.word}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    }
  })
    .then((res) => {
      console.log('검색 완')
      searchMovies.value = res.data.movies
      searchPeople.value = res.data.people
      searchGenres.value = res.data.genres
      console.log(res.data.movies)
    })
    .catch((err) => {
      // window.alert(`No related movies or actors with ${ to.params.word }`)
      console.log(err)
    })
  
  // axios({
  //   method: 'get',
  //   url: `${store.API_URL}/api/v1/genre/${to.params.word}/`,
  //   headers: {
  //     Authorization: `Token ${store.token}`,
  //   }
  // }).then((res) => {
  //   searchGenres.value = res.data.movies
  // }).catch((err) => {
  //   console.log(err)
  //   // window.alert(`No related genres with '${ route.params.word }''`)
  // })
})

</script>

<style scoped>
.mc-3 {
  color: #FBBEDE
}
</style>