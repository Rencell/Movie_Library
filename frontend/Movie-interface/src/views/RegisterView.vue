<script setup>
import movieService from '../api/movieService';
import { reactive, ref } from 'vue';

const obj = ref([])
const errorAlert = ref([])
const formData = reactive({

});

function handleUpload(event) {
    const file = event.target.files[0];
    if (file) {
        formData.image = file;
    }
}
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

function createData(event) {
    event.preventDefault();
    movieService.create(formData)
        .then(response => {

            clearFormData()
            errorAlert.value = []
        })
        .catch(e => {
            const tryko = e.response.data
            errorAlert.value = tryko
        });

}

function clearFormData() {
    // for (const key in formData) {
       
     //   delete formData[key];
    //}

}


getData()
</script>

<template>

    <div v-for="key, value in errorAlert"
        class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <strong class="font-bold">{{ value }}</strong>
        <span class="block sm:inline"> : {{ key[0] }}</span>
        <span class="absolute top-0 bottom-0 right-0 px-4 py-3">
            <svg class="fill-current h-6 w-6 text-red-500" role="button" xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20">
                <title>Close</title>
                <path
                    d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z" />
            </svg>
        </span>
    </div>



    <form @submit="createData" class="flex flex-col w-60 p-2 gap-3">

        <label for="name">Name: </label>
        <input class="border-2" v-model="formData.name" type="text" id="name" placeholder="name...">
        <label for="duration">Duration: </label>
        <input class="border-2" v-model="formData.duration" type="number" id="duration" placeholder="type...">
        <label for="rating">Rating: </label>
        <input class="border-2" v-model="formData.rating" type="number" id="rating" placeholder="type...">
        <label for="type">Type: </label>
        <input class="border-2" v-model="formData.typ" type="text" id="type" placeholder="type...">
        <input type="file" @change="handleUpload" accept="image/*">
        <input class="p-2 bg-green-500 mt-2 rounded" type="submit" value="Submit">
    </form>
</template>