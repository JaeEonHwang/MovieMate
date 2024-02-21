<template>
  <li class="list-group-item list-group-item-dark" @click="goDetail(comment.movie.id)">
    <div class="d-flex justify-content-between">
      <h3>{{ comment.content }}</h3>
      <p>{{ comment.movie.title }}</p>
    </div>
  </li>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';

const props = defineProps({
  comment: Object,
})
const router = useRouter()

const goDetail = ((id) => {
  router.push({ name: 'MovieDetailView', params: { id: id }})
})
</script>

<style scoped>

</style>