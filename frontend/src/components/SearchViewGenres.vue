<template>
  <div class="col"  >
    <div class="card h-100">
      <img :src="image" class="card-img-top" alt="..." @click="goDetail(id)">
      <div class="card-body">
        <h5 class="card-title text-center" @click="goDetail(id)">{{ title }}</h5>
        <button class="btn btn-secondary" @click="likeF" v-if="mylike">unlike</button>
        <button class="btn btn-primary" @click="likeF" v-else="mylike">like</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios';
const router = useRouter()
const store = useCounterStore()
console.log('장르카드')
const mylike = ref(false)
const image = ref('')
const title = ref('')
const id = ref(0)
const props = defineProps({
  movie: Object,
})
title.value = props.movie.title
id.value = props.movie.id
if (props.movie.images.length > 0) {
  image.value = props.movie.images[0].path
} else {
  image.value = 'https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-for-website-design-or-mobile-app-no-photo-available_87543-11093.jpg'
}
for (const likeuser of props.movie.like_user) {
    if (likeuser.username === store.username0) {
      console.log('좋아요 바꾸기')
      mylike.value = true
    }
  }

const likeF = (() => {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/likes/${id.value}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    }
  })
  .then((res) => {
    console.log('좋아요 누름')
    console.log(mylike.value)
    if (res.data.me) {
      mylike.value = true
    }
    else {
      mylike.value = false
    }
    console.log(mylike.value)
  })
  .catch((err) => {
    console.log(err)
  })
})

const goDetail = ((id) => {
  router.push({ name: 'MovieDetailView', params: { id: id }})
})




</script>

<style scoped>
/* img {
  width: 100%;
  height: 70%;
} */
/* .col {
  width: 15%;
  height: 600px;
} */
</style>