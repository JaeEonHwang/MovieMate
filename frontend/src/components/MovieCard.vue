<!-- <template>
  <div>

  </div>
</template>

<script setup>
export default {
 props: {
  movie: {
    requried: true,
  },
  genres: {
    requried: true,
  }
 },
 computed: {
  posterPath(){
    return "https://image.tmdb.org/t/p/w500/" + this.movie.poster_path
  }
 },
 methods: {
  genretypeName(genreId, index) {
    for(const item of this.genres) {
      if(item.id == genreId){
        if(this.movie.genre_ids.length - 1 == index)
      }
    }
  }
 }

}

</script>

<style>

</style> -->