<template>
    <!-- <div>
			<div class="item" @click="goDetail(id)">
          <div class="card">
            <img :src="path" class="card-img-top" alt="...">
            <div class="card-body">
              <p class="card-text text-center">{{ title }}</p>
            </div>
          </div>
			</div>
    </div> -->
    <v-card
      class="item"
      theme="dark"
      style="width: 341px; height: 191px"
      @click="goDetail(id);"
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

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const router = useRouter()

const props = defineProps({
	movie: Object,
})
const path = ref({})
const title = ref('')
const id = ref(0)
if (props.movie.images.length > 0) {
  path.value = props.movie.images[0].path
} else {
  path.value = 'https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-for-website-design-or-mobile-app-no-photo-available_87543-11093.jpg'
}

title.value = props.movie.title
id.value = props.movie.id


const goDetail = ((id) => {
  router.push({ name: 'MovieDetailView', params: { id: id }})
})
</script>


<style scoped>
html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  background-color: #d1d1d1;
}

h1 {
  font-family: Arial;
  color: red;
  text-align: center;
}

.wrapper {
  display: grid;
  grid-template-columns: repeat(3, 100%);
  overflow: hidden;
  scroll-behavior: smooth;
}

.wrapper section {
  width: 100%;
  position: relative;
  display: grid;
  grid-template-columns: repeat(5, auto);
  margin: 20px 0;
}

.item {
  padding: 0 2px;
  transition: 250ms all;
}

.item:hover {
  margin: 0 40px;
  transform: scale(1.2);
}

a {
  position: absolute;
  color: #fff;
  text-decoration: none;
  font-size: 6em;
  background: rgb(0, 0, 0);
  width: 80px;
  padding: 20px;
  text-align: center;
  z-index: 1;
}
img {
  width: 341px;
  height: 191px;
}
a:nth-of-type(1) {
  top: 0;
  bottom: 0;
  left: 0;
  background: linear-gradient(-90deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 1) 100%);
}

a:nth-of-type(2) {
  top: 0;
  bottom: 0;
  right: 0;
  background: linear-gradient(90deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 1) 100%);
}

.card-img-container {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
}

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

@media only screen and (max-width: 600px) {
  .wrapper {
    grid-template-columns: 100%;
  }

  .wrapper section {
    grid-template-columns: repeat(1, auto);
  }

  .item:hover {
    margin: 0; /* Remove margin on hover for smaller screens */
    transform: scale(1);
  }

  a.arrow__btn {
    display: none;
  }
}
</style>