<template>
  <div class="mx-5">
    <div class="d-flex justify-content-between">
      <img :src="profile" alt="" class="main">
      <img :src="profile1" alt="" class="main">
      <img :src="profile2" alt="" class="main">
      <img :src="profile3" alt="" class="main">
    </div>
    <!-- <img :src="profile" alt=""> -->
    <div class="d-flex my-5 align-items-center">
      <h1 class="mx-5">{{ name }}</h1>
      <h3>{{ birthday }}</h3>
    </div>
    <!-- 출연 영화 -->
    <div class="my-4 mx-4">
      <h3>Movies</h3>
    </div>
    <div>
      <PersonMovie :movies="movies" id="movies" />  <!-- 관련된 영화로 바꿔야 함; store/movie.js에서 코드 수정(token 보고)-->
    </div>
    <!-- <div class="row row-cols-5">
      <template v-for="movie in movies" class="col">
        <template v-if="movie.movie.images.length > 0 && movie.movie.images[0].type === 1">
          <div class="card" style="width: 18rem;" @click="goDetail(movie.movie.id)">
            <img :src="movie.movie.images[0].path" class="card-img-top" alt="...">
            <div class="card-body">
              <p class="card-text">{{ movie.movie.title }}</p>
            </div>
          </div>
        </template>
      </template>
    </div> -->
    <!-- <h3>사진</h3>
    <div class="row row-cols-4">
      <img class="col sub" v-for="photo in photos" :src="photo.profile_path" alt="">
    </div> -->
    <div class="my-4 mx-4">
      <h3>Photos</h3>
    </div>
    <div>
      <Profile :posters="photos" id="photo" />  <!-- 관련된 영화로 바꿔야 함; store/movie.js에서 코드 수정(token 보고) -->
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue'
import MovieRcmd from '@/components/MovieRcmd.vue'
import Profile from '@/components/Profile.vue'
import MovieVideo from '@/components/MovieVideo.vue'
import MoviePhoto from '@/components/MoviePhoto.vue'
import PersonMovie from '@/components/PersonMovie.vue'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const profile = ref('')
const profile1 = ref('')
const profile2 = ref('')
const profile3 = ref('')
const photos = ref([])
const name = ref('')
const birthday = ref('')
const movies = ref([])
axios({
  method: 'get',
  url: `http://127.0.0.1:8000/api/v1/person/${route.params.id}/`,
  headers: {
    Authorization: `Token ${store.token}`,
  }
})
.then((res) => {
  if (res.data.profile.length > 1) {
    profile.value = res.data.profile[0].profile_path
    profile1.value = res.data.profile[1].profile_path
    profile2.value = res.data.profile[2].profile_path
    profile3.value = res.data.profile[3].profile_path
    photos.value = res.data.profile
    console.log(photos)
  } else {
    profile.value = 'https://media.licdn.com/dms/image/C5103AQF1DVMwbnnVSA/profile-displayphoto-shrink_800_800/0/1586363789729?e=2147483647&v=beta&t=K20NJD_yB77ehGVpbouv2Q-i5H2i8EyNSexdxASBOJ8'
  }
  name.value = res.data.name_en
  birthday.value = res.data.birthday
  movies.value = res.data.credits
})

const goDetail = ((id) => {
  router.push({ name: 'MovieDetailView', params: { id: id }})
})
</script>

<style scoped>
.main {
  height: 600px;
}
.sub{
  width: 150px;
  height: 191px;
}
</style>