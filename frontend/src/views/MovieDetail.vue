<template>
  <div>
    <div class="top d-flex justify-content-center">
      <!-- <v-card class="mx-auto my-auto" width="1280px" max-height="840px" theme="dark"> -->
        <v-img :src="backdrop" class="d-block" alt="..." width="1280px" max-height="840px">
          <v-row class="fill-height align-end">
            <v-col>
              <span class="white--text">{{ title }}</span>
            </v-col>
          </v-row>
        </v-img>
      <!-- </v-card> -->
    </div>
    <div class="my-8 mx-4">
      <v-row>
        <v-col>
          <h2>{{ title }}</h2>
        </v-col>
        <v-col>
        <!-- 좋아요 -->
          <!-- {{ mylike }} -->
          <v-btn class="btn btn-primary" style="background-color: #A44CD3;" @click="likeF" v-if="mylike">liked</v-btn>
          <v-btn class="btn btn-primary" outlined style="outline-width: 2px; outline-color: #A44CD3;"  @click="likeF" v-else="mylike">like</v-btn>
        </v-col>
      </v-row>
    </div>

    <!-- Genre Section -->
    <div class="my-4 mx-4">
      <v-row>
        <v-col class="d-flex">
          <h4 class="my-6">Genre</h4>
          <v-container class="mb-16" max-width="100%">
            <v-row align="left" justify="left">
              <v-col v-for="genre in genres" :key="genre.id" cols="12" sm="6" md="4" lg="2">
                <v-card @click="goGenreDetail(genre.name_en)">
                  <v-card-title>#{{ genre.name_en }}</v-card-title>
                </v-card>
              </v-col>
            </v-row>
          </v-container>
        </v-col>
      </v-row>
    </div>

    <div class="my-4 mx-4">
      <h3>Actors</h3>
    </div>
    <div class="my-4 mx-8">
      <v-container class="mb-16">
        <v-row align="left" justify="center">
          <v-col
            v-for="actor in actors"
            cols="auto"
          >
          <!-- <div class="row row-cols-4"> -->
            <v-card
              class="mx-auto d-flex align-items-center"
              width="500"
              height="230"
              :actor="actor"
              style="background-color: rgba(64, 64, 64, 0.2); border-width: 2px; border-color: darkgray;"
              elevation="2"
              >
              <!-- <template v-for="actor in actors" class="col"> -->
                <template v-if="actor.person.profile.length > 0">
                  <v-card-item style="border-width: 2px; border-color: beige; width: 100%;"  @click="goPersonDetail(actor.person.id)">
                    <v-row>
                      <v-col class="mx-auto py-auto px-auto d-flex justify-content center align-items-center">
                        <v-avatar class="mx-auto" style="width: 9rem; height: 9rem;" outlined >
                          <img :src="actor.person.profile[0].profile_path" class="card-img-top" alt="...">
                        </v-avatar>
                      </v-col>
                      <v-col>
                        <div class="card-body">
                          <v-card-text>
                            <h7>Name</h7><br>
                            <h5>{{ truncateText(actor.person.name_en, 20) }}</h5>
                          </v-card-text>
                          <v-card-text>
                            <h7>Role</h7><br>
                            <h5>{{ truncateText(actor.character, 20) }}</h5>
                          </v-card-text>
                        </div>
                      </v-col>    
                    </v-row>
                  </v-card-item>
                </template>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>

    <!-- 댓글 입력 -->
    <v-container>
      <v-row align="left" justify="left">
        <!-- 댓글 목록 -->
        <v-col cols="12" sm="8"> <!-- 왼쪽 기준으로 2/3 너비 -->
          <v-list class="mb-8">
            <v-list-item-group>
              <v-list-item v-for="comment in comments" :key="comment.id">
                <v-list-item-content class="d-flex justify-content-between"><div><strong class="me-5">{{ comment.user.username }} : </strong>{{ comment.content }}</div><div class="d-flex"><p>{{ comment.created_at.slice(0,10) }}</p><p class="ms-3">{{ comment.created_at.slice(11,16) }}</p></div></v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        <!-- 댓글 입력 -->
          <v-row class="mb-3">
            <v-col cols="10">
              <input type="text" class="form-control" placeholder="Leave a Comment Here!" aria-label="Recipient's username" aria-describedby="button-addon2" v-model.trim="reply" @keyup.enter="createReply">
            </v-col>
            <v-col cols="2">
              <button @click="createReply" style="background-color: #A44CD3;" class="btn btn-outline-secondary" type="button" id="button-addon2">Add</button>
            </v-col>
          </v-row>
        </v-col>
        
      </v-row>
    </v-container>

    <!-- Related Movies-->
    <div class="my-4 mx-4">
      <h3>Related Movies</h3>
    </div>
    <div>
      <MovieRcmd :movies="related_movies" id="RelatedMovies" />  <!-- 관련된 영화로 바꿔야 함; store/movie.js에서 코드 수정(token 보고)-->
    </div>
    <!-- 원래 있던 코드(Related Movies)-->
    <!-- <div class="row row-cols-5 mb-8 mx-8">
      <template v-for="movie in related_movies" class="col">
        <template v-if="movie.images.length > 0 && movie.images[0].type === 1">
          <div class="card col g-3"  @click="goDetail(movie.id)">
            <img :src="movie.images[0].path" class="card-img-top" alt="...">
            <div class="card-body">
              <p class="card-text">{{ movie.title }}</p>
            </div>
          </div>
        </template>
      </template>
    </div> -->

    <!-- Youtube Videos -->
    <div class="my-4 mx-4">
      <h3>Photos</h3>
    </div>
    <div>
      <MoviePhoto :posters="posters" id="photo" />  <!-- 관련된 영화로 바꿔야 함; store/movie.js에서 코드 수정(token 보고) -->
    </div>

    <!-- Youtube Videos 원래 있던 코드-->
    <!-- <div class="row row-cols-4">
      <div v-for="video in videos" class="col">
        <iframe  width="448" height="252" :src="video.youtube_path" frameborder="0" allowfullscreen></iframe>
        <p>{{ video.title }}</p>
      </div>
    </div> -->

    <!-- Related Pictures -->
    <div class="my-4 mx-4">
      <h3>Youtube Videos</h3>
    </div>
    <div>
      <MovieVideo :videos="videos" id="video" />  <!-- 관련된 영화로 바꿔야 함; store/movie.js에서 코드 수정(token 보고)-->
    </div>

    <!-- 원래 있던 Pictures-->
    <!-- <div class="row row-cols-4">
      <img class="col" v-for="image in posters" :src="image.path" alt="">
    </div> -->
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter, onBeforeRouteUpdate, onBeforeRouteLeave } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import { useMovieStore } from '@/stores/movie'
import MovieRcmd from '@/components/MovieRcmd.vue'
import axios from 'axios'
import PeopleView from '@/views/PeopleView.vue'
import MoviePhoto from '@/components/MoviePhoto.vue'
import MovieVideo from '@/components/MovieVideo.vue'

const route = useRoute()
const movie = ref({})
const router = useRouter()
const movieStore = useMovieStore()
const store = useCounterStore()
const movieId = ref(route.params.id)
const title = ref('')
const backdrop = ref('')
const posters = ref([])
const genres = ref([])
const keywords = ref([])
const related_movies = ref([])
const actors = ref([])
const videos = ref([])
const mylike = ref(false)
const likes = ref(0)
const reply = ref('')
const comments = ref([])
const topRated = ref([])
topRated.value = movieStore.topRated

// 디테일 페이지로 들어오면서 정보 요청
axios({
  method: 'get',
  url: `${store.API_URL}/api/v1/movie/${movieId.value}/`,
  headers: {
    Authorization: `Token ${store.token}`,
  }
}).then((res) => {
  movie.value = res.data
  title.value = res.data.title
  if (res.data.images.length > 0) {
    backdrop.value =res.data.images[0].path
  }
  posters.value = res.data.images
  genres.value = res.data.genres
  keywords.value = res.data.keywords
  related_movies.value = res.data.related_movie
  actors.value = res.data.credits.slice(0,res.data.credits.length-2)
  videos.value = res.data.videos
  for (const likeuser of res.data.like_user) {
    if (likeuser.username === store.username0) {
      mylike.value = true
    }
  }
  comments.value = res.data.comment.reverse()
  console.log(posters.value)
})
.catch((err) => {
  // 영화 정보 없는 경우가 있음, alert 필요
  console.log(err)
})

// 다른 영화 디테일 페이지로 이동
const goDetail = ((id) => {
  router.push({ name: 'MovieDetailView', params: { id: id }})
})
// 페이지 업데이트 될 때 정보 업데이트
onBeforeRouteUpdate((to, from) => {
  movieId.value = to.params.id
  axios({
  method: 'get',
  url: `${store.API_URL}/api/v1/movie/${movieId.value}/`,
  headers: {
    Authorization: `Token ${store.token}`,
  }
  }).then((res) => {
    movie.value = res.data
    movie.value = res.data
    title.value = res.data.title
    if (res.data.images.length > 0) {
      backdrop.value =res.data.images[0].path
    }
    posters.value = res.data.images
    genres.value = res.data.genres
    keywords.value = res.data.keywords
    related_movies.value = res.data.related_movie
    actors.value = res.data.credits.slice(0,res.data.credits.length-2)
    videos.value = res.data.videos
    for (const likeuser of res.data.like_user) {
      if (likeuser.username === store.username0) {
        mylike.value = true
      }
    }
    comments.value = res.data.comment.reverse()
    window.scrollTo(0,0)

  })
  .catch((err) => {
  // 영화 정보 없는 경우가 있음, alert 필요
  console.log(err)
  })
})


// 영화 좋아요 누르는 함수
const likeF = (() => {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/likes/${movieId.value}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    }
  })
  .then((res) => {
    likes.value = res.data
    if (res.data.me) {
      mylike.value = true
    }
    else {
      mylike.value = false
      
    }
  })
  .catch((err) => {
    console.log(err)
  })
})


// 댓글 남기는 함수
const createReply = function () {
  axios({
    method:'post',
    url: `${store.API_URL}/api/v1/comments/movie/${movieId.value}/`,
    data: {
      content: reply.value
    },
    headers: {
      Authorization: `Token ${store.token}`,
    }
  })
  .then((res) => {
    comments.value.unshift(res.data)
    reply.value=''
  })
  .catch((err) => {
    console.log(err)
  })
}

// 검색창으로 이동하는 함수
const searchWord = ref('')
const search = (() => {
  router.push({ name: 'SearchView', params: { word: searchWord.value }})
})


const goPersonDetail = ((id) => {
  router.push({ name: 'PeopleView', params: { id: id }})
})

const goGenreDetail = ((genre) => {
  router.push({ name: 'GenreView', params: { genre: genre }})
})

// 글자 자르는 함수
const truncateText = ((text, length) => {
  if (text.length > length) {
    return text.substring(0, length) + '...';
  } else {
    return text;
  }
})

const props = defineProps({
	movies: Array,
	id: String,
	title: String,
})


const scrollContent = (scrollAmount) => {
	document.querySelector(`#${props.id}`).scrollLeft += scrollAmount
};
</script>

<style scoped>
.d-block {
  width: 90%;
}
.card-img-top {
  height: 300px;
}
</style>