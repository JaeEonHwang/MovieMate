<template>
  <div class="carousel-item">
    <div class="d-flex justify-content-center">
      <img :src="path" class="d-block" alt="...">
      {{ movie }}
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, defineProps } from 'vue'
import { onBeforeRouteUpdate,  } from 'vue-router'
import { useCounterStore } from '@/stores/counter';

const counterStore = useCounterStore()

const props = defineProps({
  backdrop: Object,
})

const path = ref('')
const movie = ref('')
path.value = props.backdrop.path
movie.value = props.backdrop.movie

onBeforeRouteUpdate((to, from) => {
  path.value = props.backdrop.path
  movie.value = props.backdrop.movie
})


</script>

<style scoped>
.d-block {
  width: 90%;
}
</style>