<template>
  <v-app>
    <!-- <v-carousel>
      <v-carousel-item
        :src="path"
        class="carousel-img-container"
      ></v-carousel-item>

      <v-carousel-item
        src="https://cdn.vuetifyjs.com/images/cards/hotel.jpg"
        cover
      ></v-carousel-item>

      <v-carousel-item
        src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
        cover
      ></v-carousel-item>
    </v-carousel> -->

    <!-- Carousel Example Code -->
    <!-- <div id="carouselExample" class="carousel slide mb-5">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <div class="d-flex justify-content-between">
            <img src="https://image.tmdb.org/t/p/original/tmU7GeKVybMWFButWEGl2M4GeiP.jpg" class="d-block" alt="...">
            <img src="https://image.tmdb.org/t/p/original/tmU7GeKVybMWFButWEGl2M4GeiP.jpg" class="d-block" alt="...">
            <img src="https://image.tmdb.org/t/p/original/tmU7GeKVybMWFButWEGl2M4GeiP.jpg" class="d-block" alt="...">
          </div>
        </div>
        <div class="carousel-item">
          <div class="d-flex justify-content-between">
            <img src="https://image.tmdb.org/t/p/original/kXfqcdQKsToO0OUXHcrrNCHDBzO.jpg" class="d-block" alt="...">
            <img src="https://image.tmdb.org/t/p/original/kXfqcdQKsToO0OUXHcrrNCHDBzO.jpg" class="d-block" alt="...">
            <img src="https://image.tmdb.org/t/p/original/kXfqcdQKsToO0OUXHcrrNCHDBzO.jpg" class="d-block" alt="...">
          </div>
        </div>
        <div class="carousel-item">
          <div class="d-flex justify-content-between">
            <img src="https://image.tmdb.org/t/p/original/3f92DMBTFqr3wgXpfxzrb0qv8nG.jpg" class="d-block" alt="...">
            <img src="https://image.tmdb.org/t/p/original/3f92DMBTFqr3wgXpfxzrb0qv8nG.jpg" class="d-block" alt="...">
            <img src="https://image.tmdb.org/t/p/original/3f92DMBTFqr3wgXpfxzrb0qv8nG.jpg" class="d-block" alt="...">          
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div> -->


    <v-container>
      <MovieRcmd :movies="topRated" id="toprated" title='Top Rated Movies' />
      <MovieRcmd :movies="genreLike.movies" id="genrelike" :title="genreLike.name" />
      <MovieRcmd :movies="upcoming" id="upcoming" title="Upcoming Movies"/>
      <MovieRcmd :movies="genreLike2.movies" id="genrelike2" :title="genreLike2.name" />
      <MovieRcmd :movies="now_playing" id="nowplaying" title="Now Playing Movies" />
      <!-- <MovieRcmd :movies="liked_genres" id="likedgenres" title="{{ username }}님을 위한 추천 영화" /> -->
    </v-container>
  </v-app>
</template>

<script setup>
import MovieRcmd from '@/components/MovieRcmd.vue'
import { useMovieStore } from '@/stores/movie'
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'

const movieStore = useMovieStore()
const store = useCounterStore()
const topRated = ref([])
topRated.value = movieStore.topRated

const upcoming = ref([])
upcoming.value = movieStore.upcoming

const now_playing = ref([])
now_playing.value = movieStore.nowPlaying

// post 요청 보내서 값 확인 한 다음 Carousel 만들기
// const path = ref({})
// if (topRated.movies.images.length > 0) {
//   path.value = topRated.movie.images[0].path
// } else {
//   path.value = 'https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-for-website-design-or-mobile-app-no-photo-available_87543-11093.jpg'
// }

const genreLike = ref([])
const genreLike2 = ref([])
axios({
  method: 'get',
  url: `http://127.0.0.1:8000/api/v1/userfavorite/`,
  headers: {
    Authorization: `Token ${store.token}`,
  }
})
.then((res) => {
  genreLike.value = res.data.genre
  genreLike2.value = res.data.genre2
})
.catch((err) => {
  console.log(err)
})

</script>

<style scoped>

img {
  width: 33%;
}

.carousel-img-container {
  max-width: 100%;
  max-height: 640px;
  
}
</style>