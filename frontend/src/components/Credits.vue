<template>
	<div>
		<div class="btn-group" role="group" aria-label="Basic checkbox toggle button group">
			<template v-for="actor in props.credit.cast">
				<input type="checkbox" class="btn-check" id="btncheck1" autocomplete="off">
				<label class="btn btn-outline-primary" for="btncheck1">{{ actor.name }}</label>
			</template>
		</div>
	</div>
</template>

<script setup>
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { ref, onBeforeMount } from 'vue'

const props = defineProps({
	credit: Object,
	title: String,
})

const director = ref({})
const actors = ref([])

const id=ref(0)


// director.value = props.credits.director
// actors.value = props.credits.cast
</script>

<style scoped>

</style>