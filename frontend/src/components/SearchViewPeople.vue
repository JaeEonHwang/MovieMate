<template>
  <div class="col">
    <div class="card h-100" @click="goDetail(id)">
      <img :src="image" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title text-center">{{ name }}</h5>
      </div>
    </div>
  </div>
</template>

<script setup>
import { isCancel } from 'axios';
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const image = ref('')
const name = ref('')
const id = ref(0)
const props = defineProps({
  person: Object,
})
name.value = props.person.name_en
const profiles = props.person.profile
id.value = props.person.id
if (profiles.length > 0) {
  image.value=profiles[0].profile_path
} else {
  image.value='https://media.licdn.com/dms/image/C5103AQF1DVMwbnnVSA/profile-displayphoto-shrink_800_800/0/1586363789729?e=2147483647&v=beta&t=K20NJD_yB77ehGVpbouv2Q-i5H2i8EyNSexdxASBOJ8'
}

const goDetail = ((id) => {
  router.push({ name: 'PeopleView', params: { id: id }})
})


</script>

<style scoped>

</style>