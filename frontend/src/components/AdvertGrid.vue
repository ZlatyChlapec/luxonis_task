<script setup lang="ts">
import {ref, onMounted, nextTick} from "vue";
import Masonry from "masonry-layout";

interface Advert {
  images: [string];
  title: string;
  url: string;
}

const adverts = ref<[Advert] | []>([]);
const apiEndpoint = "http://127.0.0.1:8080/api/adverts/v1";
const grid = ref<HTMLDivElement | null>(null);
let masonry: Masonry;

onMounted(async () => {
  const res = await fetch(apiEndpoint);
  adverts.value = await res.json();
  document.title = adverts.value.length + " adverts";
  // Masonry needs elements to exist so we have to wait
  await nextTick(() => {
    masonry = new Masonry(grid.value!, {
      itemSelector: ".a-item",
      fitWidth: true,
    });
  });
});

function redraw(_event: Event) {
  // We need to adjust grid after images are loaded
  masonry.layout?.();
}
</script>

<template>
  <div class="mx-auto my-0" ref="grid">
    <div v-for="advert in adverts"
         class="a-item m-2 flex flex-col items-center justify-center max-w-sm">
      <img class="rounded-lg shadow-md" :src="advert.images[0]" alt="" @load="redraw">
      <div class="w-full -mt-9 bg-white rounded-b-lg dark:bg-gray-800/40">
        <h1 class="py-2 text-center">
          <a class="font-semibold tracking-wide text-sm text-gray-700
          dark:text-gray-200 hover:underline"
             tabindex="0"
             role="link"
             :href="advert.url">{{ advert.title }}</a>
        </h1>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
