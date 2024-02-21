<template>
	<div>
		<div class="d-flex justify-content-between" show-arrows="hover">
			<button @click="scrollContent(-348)" class="btn btn-dark">◁</button>
			<h2>{{ title }}</h2>
			<button @click="scrollContent(348)" class="btn btn-dark">▷</button>
		</div>
		<ul class="list-group list-group-horizontal overflow-hidden" :id="id">
			<template v-for="movie in movies">
        <template v-if="movie.movie.images.length > 0 && movie.movie.images[0].type === 1">
          <li>
            <MovieRcmdCard :movie="movie.movie" />  
          </li>
        </template>
			</template>
		</ul>
	</div>  
</template>

<script setup>
import MovieRcmdCard from '@/components/MovieRcmdCard.vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { ref, onBeforeMount } from 'vue'
import { isIntegerKey } from '@vue/shared';

console.log('영화')
const props = defineProps({
	movies: Array,
	id: String,
	title: String,
})

const scrollContainer = ref(0);

const scrollContent = (scrollAmount) => {
	document.querySelector(`#${props.id}`).scrollLeft += scrollAmount
  // scrollContainer.value.scrollLeft += scrollAmount;
};
  



const store = useCounterStore()




// const movies = ref([])

// axios({
// 	method: 'get',
// 	url: `${store.API_URL}${props.path}`,
// 	headers: {
// 		Authorization: `Token ${store.token}`
// 	}
// }).then((res) => {
// 	movies.value = res.data
// }).catch((err) =>{
// 	console.log(err)
// })









</script>

<style scoped>
html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  background-color: #000;
}

h1 {
  font-family: Arial;
  color: red;
  text-align: center;
}
p {
	text-align: center;
}

ul {
  /* display: grid; */
  grid-template-columns: repeat(3, 100%);
  overflow: hidden;
  scroll-behavior: smooth;
}
li {
	/* margin-top: 20px; */
	margin-bottom: 20px;
	list-style-type: none;
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
img {
	width: 341px;
	height: 191px;
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