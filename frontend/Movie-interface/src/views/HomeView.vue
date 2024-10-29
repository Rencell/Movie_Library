<script setup>
import movieService from '../api/movieService';
import { ref } from 'vue';

const obj = ref([])

function getData() {
  movieService.getAll()
    .then(response => {
      const index = response.data
      obj.value = index
    })
    .catch(e => {
      alert(e.data)

    });
}
function destroy(id) {
  movieService.destroy(id)
    .then(response => {
      console.log(response)
      getData()
    })
    .catch(e => {
      console.log(e)
    });
}

getData()
</script>

<template>
  <main>
    <div class="flex">
      <ul>
        <li v-for="objs in obj" class="flex justify-between">
          
          {{ objs.name }}

          <div class="h-40 ">
            <img class="h-full" :src="objs.image" alt="">
          </div>
          <button @click="destroy(objs.id)" class="p-3 bg-red-400">delete</button>
        </li>

      </ul>
    </div>
  </main>
</template>
