<template>
  <v-container>
    <!-- 유저 프로필 정보 -->
    <v-row align="center" class="my-4">
      <v-avatar size="150">
        <!-- 유저 프로필 사진 -->
        <v-img :src="user.profilePicture" :alt="user.username"></v-img>
      </v-avatar>
      <v-col>
        <!-- 유저명 -->
        <h2>{{ user.username }}</h2>
        <!-- 팔로워/팔로잉 수 -->
        <!-- <div>Followers : {{ user.followers }}  Following : {{ user.following }}</div> -->
        <!-- 팔로우/언팔로우 버튼 -->
        <!-- <v-btn @click="toggleFollow" :loading="loading" :disabled="loading">
          {{ following ? 'Unfollow' : 'Follow' }}
        </v-btn> -->
      </v-col>
    </v-row>

    <!-- 댓글 탭 -->
    <!-- <v-tabs v-model="tab" grow> -->
      <!-- <v-tab v-for="commentTab in commentTabs" :key="commentTab.id">
        {{ commentTab.name }}
      </v-tab> -->
      <!-- <v-tab></v-tab> -->
      <!-- <v-tab-item v-for="commentTab in commentTabs" :key="commentTab.id">
        <v-container> -->
          <!-- 댓글 목록 또는 해당 댓글 내용을 표시하는 부분 -->
          <!-- <v-row>
            <v-col v-for="comment in comments" :key="comment.id">
              {{ comment.content }}
            </v-col>
          </v-row>
        </v-container>
      </v-tab-item>
    </v-tabs> -->
    <!-- {{ myMovies[0].like_user }} -->
    <v-card>
      <v-tabs v-model="tab" color="#FBBEDE" align-tabs="left" style="margin-left: 16px;">
        <v-tab :value="1">My Movies</v-tab>
        <v-tab :value="2">My comments</v-tab>
      </v-tabs>
      <v-window v-model="tab">
        <v-window-item :value="1">
          <!-- <template v-if="myMovies"> -->
            <v-container fluid>
              <v-row>
                <v-col>
                  <!-- {{ myMovies }} -->
                  <div class="row row-cols-2 row-cols-md-4 row-cols-lg-4 g-4">
                    <template v-for="movie in myMovies" >
                      
                      <!-- {{ movie }} -->
                      <!-- <SearchViewMovie :movie="movie" /> -->
                      <SearchViewMovie v-if="movie.images.length > 0 && movie.images[0].type == 1" :movie="movie"/>
                    </template>
                  </div>
                </v-col>
              </v-row>
            </v-container>
          <!-- </template> -->
        </v-window-item>

        <v-window-item :value="2">
          <!-- <template v-if="searchPeople"> -->
            <v-container fluid>
              <v-row>
                <v-col>
                  <!-- <div class="row row-cols-2 row-cols-md-4 row-cols-lg-6 g-4"> -->
                    <ul class="list-group list-group-flush">
                      <MyPageComment v-for="comment in myComments" :comment="comment"/>
                      <!-- <li class="list-group-item">An item</li>
                      <li class="list-group-item">A second item</li>
                      <li class="list-group-item">A third item</li>
                      <li class="list-group-item">A fourth item</li>
                      <li class="list-group-item">And a fifth one</li> -->
                    </ul>
                    <!-- <SearchViewPeople v-for="person in searchPeople" :person="person" /> -->
                  <!-- </div> -->
                </v-col>
              </v-row>
            </v-container>
          <!-- </template> -->
        </v-window-item>

        
      </v-window>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter'
import SearchViewMovie from '@/components/SearchViewMovie.vue';
import MyPageComment from '@/components/MyPageComment.vue'

const tab = ref(null)
const router = useRouter()
const store = useCounterStore()
const route = useRoute()
const user = ref({
  username: route.params.username,
  profilePicture: 'https://placekitten.com/150/150',
  followers: 100,
  following: 50,
});

// const following = ref(false);
// const loading = ref(false);
// const tab = ref(0);

// const commentTabs = ref([
//   { id: 0, name: '전체' },
//   { id: 1, name: '게시물' },
//   { id: 2, name: '좋아요' },
//   // 필요한 탭 추가
// ]);

// const comments = ref([
//   { id: 1, content: '테스트 댓글 1' },
//   { id: 2, content: '테스트 댓글 2' },
//   // 필요한 댓글 데이터 추가
// ]);

// const toggleFollow = async () => {
//   loading.value = true;
//   // 여기에 팔로우/언팔로우 로직을 비동기로 구현
//   // 예: await api.toggleFollow(user.id);
//   following.value = !following.value;
//   loading.value = false;
// };

const myMovies = ref([])
const myComments = ref([])

axios({
  method: 'get',
  url: `http://127.0.0.1:8000/api/v1/user/${route.params.username}/`,
  headers: {
    Authorization: `Token ${store.token}`,
  }
}).then((res) => {
  myMovies.value = res.data.movies_set
  myComments.value = res.data.comment
})



</script>

<style>

</style>