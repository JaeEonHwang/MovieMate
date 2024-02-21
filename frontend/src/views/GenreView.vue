<template>
  <div class="mx-5">
    <h1 class="m-4">{{ genre }}</h1>
    <div class="row row-cols-5 g-3 d-flex justify-content-center">
      <template v-for="movie in movies" class="col">
        <template v-if="movie.images.length > 0 && movie.images[0].type === 1">
          <!-- <div class="card m-2" style="width: 18rem;" @click="goDetail(movie.id)">
            <img :src="movie.images[0].path" class="card-img-top" alt="...">
            <div class="card-body">
              <p class="card-text">{{ movie.title }}</p>
            </div>
          </div> -->
          <v-card
            class="item mx-3"
            theme="dark"
            style="width: 341px; height: 191px"
            @click="goDetail(movie.id);"
            >
            <!-- <div class="card"> -->
              <v-img
                :src="movie.images[0].path"
                alt="Card Image"
                class="card-img-container"
                ></v-img>
              <!-- <div class="card-body">
                <v-card-title>{{ title }}</v-card-title>
              </div> -->
              <div class="card-title px-3 text-center" style="color: rgba(255, 255, 255, 0.9); background-color: rgba(0, 0, 0, 0.4);">{{ movie.title }}</div>
            <!-- </div> -->
          </v-card>
        </template>
      </template>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue'

const route = useRoute()
const router = useRouter()
const store = useCounterStore()
const movies = ref([])
const genre = ref('')
axios({
  method: 'get',
  url: `http://127.0.0.1:8000/api/v1/genre/${route.params.genre}/`,
  headers: {
    Authorization: `Token ${store.token}`,
  }
})
.then((res) => {
  movies.value = res.data.movies
  genre.value = res.data.genre.name_en
})
.catch((err) => {
  console.log(err)
})

const goDetail = ((id) => {
  router.push({ name: 'MovieDetailView', params: { id: id }})
})
</script>

<style scoped>
.card-title {
  position: absolute;
  bottom: 8%; /* 수직 중앙 정렬을 위한 조절 */
  left: 50%;
  transform: translate(-50%, 50%);
  font-size: 16px; /* 적절한 폰트 크기로 조절 */
  font-weight: 600; /* 폰트 굵기 조절 */
  transition: opacity 0.3s ease-in-out;
  opacity: 1;
  width: 90%;
}

</style>