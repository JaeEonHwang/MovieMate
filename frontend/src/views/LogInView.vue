<template>
  

  
  <v-app>
    <div class="backgroundimg"  style="padding-top: 18%;">
    <v-container fluid>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="6" lg="4">
          <v-card class="pa-4" outlined>
            <v-form @submit.prevent="handleLogIn">
              <v-text-field v-model.trim="username" label="ID"></v-text-field>
              <v-text-field v-model.trim="password" label="Password" type="password"></v-text-field>
              <v-btn type="submit" color="#A44CD3">Login</v-btn>
            </v-form>
            <v-divider class="my-4"></v-divider>

            <v-row align="center" justify="center">
              <v-col>
                <!--여기에 인라인 스타일 말고 다른 스타일을 찾아보기-->
                <span class="custom-margin-1">Create account</span><br>
                
                <v-btn @click="goToSignUp" color="#A44CD3" text>Sign Up</v-btn>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
  </v-app>

</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const router = useRouter()
const username = ref(null)
const password = ref(null)

const goToSignUp = function () {
  router.push({ name: 'SignUpView' })
}

const handleLogIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style scoped>
.backgroundimg {
  height: 100%;
  width: 100%;
  background-size: cover;
  background-image: url("https://pyxis.nymag.com/v1/imgs/678/8b4/3efde8f254542d9039e64ad2bb21964ba6-23-lalaland-yellow-dress.2x.rhorizontal.w710.jpg");
  }
</style>