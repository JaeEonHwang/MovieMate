<template>
  <div>
    <h1>{{ store.username }}님이 좋아하시는 영화를 골라주세요</h1>
    <h5>좋아하는 모든 콘텐츠를 눌러주세요.</h5>
    <h5>취향에 맞는 영화를 골라드릴게요.</h5>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const router = useRouter()

const username = store.username

// ProfilesAddView.vue 컴포넌트가 생성될 때 로그인 여부를 확인하고 로그인하지 않았다면 로그인 페이지로 이동
if (!store.isLogIn) {
  router.push({ name: 'LogInView' })
}

</script>

<style scoped>

</style>