<template>
	<div>
		<div class="d-flex m-3 justify-content-between">
			<h1 class="text-center fx-bold">Please show your movie taste!</h1>
			<button type="button" class="btn btn-success" @click="goHome">Done</button>
		</div>
		<div class="row row-cols-2 row-cols-md-4 row-cols-lg-6 g-4">
			<template v-for="movie in movies">
				<template v-if="movie.images.length > 0 && movie.images[0].type === 1">
					<StartCard :movie="movie"/>
				</template>
			</template>
		</div>
	</div>
</template>

<script setup>
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue'
import StartCard from '@/components/StartCard.vue'
import { useRouter } from 'vue-router';
const store = useCounterStore()
const movies = ref([])
const mylike = ref(false)
const router = useRouter()

axios({
  method: 'get',
  url: `http://127.0.0.1:8000/api/v1/movies/`,
  headers: {
    Authorization: `Token ${store.token}`,
  }
})
.then ((res) => {
    movies.value = res.data
})


const likeF = ((id) => {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/likes/${id}/`,
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

const goHome = () => {
	router.push({ name: 'MovieView' })
}
</script>

<style scoped>

</style>