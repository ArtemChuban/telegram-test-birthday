<script setup lang="ts">
import '@/assets/main.css'
import { RouterView } from 'vue-router'
</script>

<template>
  <main class="bg-gradient-to-b from-[#1E2A78] via-[#6E1D67] to-[#160D2C] h-dvh w-dvw p-5">
    <div class="absolute -z-10 top-1/4 left-1/3 w-72 h-72 bg-purple-500 opacity-50 blur-3xl rounded-full"></div>
    <div class="absolute -z-10 bottom-1/4 right-1/3 w-80 h-80 bg-blue-500 opacity-40 blur-3xl rounded-full"></div>
    <div class="absolute -z-10 top-1/2 left-1/2 w-96 h-96 bg-pink-500 opacity-30 blur-3xl rounded-full"></div>
    <RouterView />
  </main>
</template>
