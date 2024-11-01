<template>
  <main class="bg-slate-900" :class="modals ? 'overflow-hidden' : ''">

    <div class="p-6">
      <div class="grid gap-4">

        <div class="bg-black rounded-md">
          <img class="h-auto m-auto max-w-full rounded-lg"
            src="https://occ-0-8407-2219.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABXHrRD23-SCJ7YC30D2psLQqgEVLaxyPbl9ojlOrpPTJQNkfkvkStCvRJfMDEuRNVes4sqylWQ-tmGKVlWBWxOyI1SarTOgp8sYQ.jpg?r=a9c"
            alt="">
        </div>

        <div>
          <div class=" bg-white w-fit rounded-lg">
            <i class="bi bi-search ms-2"></i>
            <input type="text" class="outline-none p-3 rounded-lg" v-model="search">
          </div>
        </div>

        <div class="grid grid-cols-5 gap-4">
          <div v-for="objs in searchFunction" @mouseover="checkIndex = objs.id" @mouseleave="checkIndex = null"
            class="gallery" :class="{ 'active': checkIndex === objs.id }">
            <img class="h-auto max-w-full rounded-lg" :src="objs.image" alt="">
            <div class="buttons w-full flex justify-between p-3 text-2xl" :class="{ 'active': checkIndex !== objs.id }">

              <div class="flex gap-1">
                <button @click="changeCover(objs.id)">
                  <i class="bi bi-play-fill"></i>
                </button>
                <button @click="openModal(objs.id)">
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
    <Edits 
      :show-modal=modals 
      @close-modal="modals = false" 
      @get-all="getData" 
      ref="modalComponent" 
    />
  </main>

</template>

<!-- Script -->


<script setup>
import movieService from '@/api/movieService';
import Edits from '@/components/Modal/Edits.vue';
import { ref, computed, onMounted } from 'vue';

const obj = ref([])
const checkIndex = ref('')
const modals = ref(false)
const modalComponent = ref(null)

const search = ref('')
const searchFunction = computed(() => {
  const listMapping = obj.value.filter(data => {
    return data.name.toLowerCase().includes(search.value.toLowerCase())
  })

  return listMapping
})


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

function openModal(id) {
  document.body.classList.add('overflow-hidden')
  modals.value = true
  modalComponent.value.editDetails(id);
}

onMounted(()=>{
  getData()
});

</script>
