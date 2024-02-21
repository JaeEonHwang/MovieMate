<template>
  <!-- <div>
    <h1>회원가입 페이지</h1>
    <form @submit.prevent="handleSignUp">
      <label for="username">아이디 : </label>
      <input type="text" id="username" v-model.trim="username" required><br>

      <label for="password1">비밀번호 : </label>
      <input type="password" id="password1" v-model.trim="password1" required><br>

      <label for="password2">비밀번호 확인 : </label>
      <input type="password" id="password2" v-model.trim="password2" required><br>
      <v-app>
        <v-btn color="primary" type="submit">다음</v->
      </v-app>

      <h6>이미 회원이신가요?</h6>
      <button @click="goToLogin">로그인 하기</button> -->

      <!-- 소셜 로그인 구현하려다가 pass(후순위로 미뤄둠) -->
      <!-- <button @click="">Google 계정으로 회원가입하기</button> -->
    <!--</form>
  </div> -->
  <v-app>
    <div class="backgroundimg" style="padding-top: 18%;">
    <v-container fluid >
      <v-row justify="center">
        <v-col cols="12" sm="8" md="6" lg="4" >
          <v-card class="pa-4" outlined >
            <v-form @submit.prevent="handleSignUp">
              <v-text-field v-model.trim="username" label="ID" required></v-text-field>
              <v-text-field v-model.trim="password1" label="Password" type="password" required></v-text-field>
              <v-text-field v-model.trim="password2" label="Password Verification" type="password" required></v-text-field>

              <v-btn type="submit" color="#A44CD3">Next</v-btn>
            </v-form>
            <v-divider class="my-4"></v-divider>

            <v-row align="center" justify="center">
              <v-col>
                <!--여기에 인라인 스타일 말고 다른 스타일을 찾아보기-->
                <span class="custom-margin-1">Already have an account?</span><br>
                
                <v-btn @click="goToLogin" color="#A44CD3" text>Go to Log In</v-btn>
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
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const router = useRouter()

const handleSignUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}

const goToLogin = function () {
  router.push({ name: 'LogInView' })
}
</script>

<style>
.custom-margin-1 {
  margin-right: 10px;
  margin-left: 10px;
  margin-top: 10px;
  padding-bottom: 10px;
}

.mc-text-1 {
  color: #A44CD3;
}

.mc-text-2 {
  color: #E090DF;
}

.mc-text-3 {
  color: #FBBEDE;
}
.backgroundimg {
  height: 100%;
  width: 100%;
  background-size: cover;
  background-image: url("https://pyxis.nymag.com/v1/imgs/678/8b4/3efde8f254542d9039e64ad2bb21964ba6-23-lalaland-yellow-dress.2x.rhorizontal.w710.jpg");
  }
</style>
