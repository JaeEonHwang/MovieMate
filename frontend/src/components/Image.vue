<template>
  <div>
    <img src="" alt="">
  </div>
</template>

<script setup>
import { ref } from 'vue';
const params = defineProps({
  image: Object,
})

const path = ref('')
path.value = params.image.path

</script>

<style  scoped>

</style>