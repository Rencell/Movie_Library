<script setup>
import { data } from 'autoprefixer';
import movieService from '../api/movieService';
import { ref } from 'vue';

const obj = ref([])
const checkIndex = ref('')

async function getData() {
  try {
    const response = await movieService.getAll();
    obj.value = response.data
  } catch (error) {
    alert(error.data)
  }
}
async function destroy(id) {
  try {
    const response = await movieService.destroy(id)
    obj.value = response.data
    getData()
  } catch (error) {
    alert(error.data)
  }
}

function handleInput(event){
  const dataHandle = event.target.value
  const listMapping = obj.value.filter(data => {
    return data.name.toLowerCase().includes(dataHandle.toLowerCase())
  })

  
  if(listMapping){
    obj.value = listMapping
    console.log(obj.value)
  }

  if(dataHandle === ""){
    getData()
  }
}

getData()
</script>

<template>
  <main class="bg-slate-900">

    <div class="p-6">
      <div class="grid gap-4">
        <div class="bg-black rounded-md">
          <img class="h-auto m-auto max-w-full rounded-lg"
            src="https://occ-0-8407-2219.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABXHrRD23-SCJ7YC30D2psLQqgEVLaxyPbl9ojlOrpPTJQNkfkvkStCvRJfMDEuRNVes4sqylWQ-tmGKVlWBWxOyI1SarTOgp8sYQ.jpg?r=a9c" alt="">
        </div>

        <div>
          <div class=" bg-white w-fit rounded-lg">
            <i class="bi bi-search ms-2"></i>
            <input type="text" class="outline-none p-3 rounded-lg"  @input="handleInput">
          </div>
        </div>
        <div class="grid grid-cols-5 gap-4">
          
          
          
          <div v-for="objs in obj" @mouseover="checkIndex = objs.id" @mouseleave="checkIndex = null" class="gallery"
            :class="[checkIndex === objs.id ? 'active' : '']">
            <img class="h-auto max-w-full rounded-lg" :src="objs.image" alt="">
            <div class="buttons w-full flex justify-between p-3 text-2xl"
              :class="[checkIndex === objs.id ? '' : 'active']">

              <div class="flex gap-1">
                <button @click="changeCover(objs.id)">
                  <i class="bi bi-play-fill"></i>
                </button>
                <button>
                  <i class="bi bi-cloud-download-fill"></i>
                </button>
              </div>

              <button @click="destroy(objs.id)">
                <i class="bi bi-trash-fill"></i>
              </button>


            </div>
          </div>
        </div>
      </div>
    </div>

  </main>
</template>
