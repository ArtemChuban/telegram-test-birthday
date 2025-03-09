<script setup lang="ts">
import '@/assets/main.css'
import { RouterView } from 'vue-router'
import useUser from '@/stores/user'
import router from '@/router'

const { start_param: startParam = '' } = window.Telegram.WebApp.initDataUnsafe || {}
router.push(`/${startParam}`)
useUser().fetch()
</script>

<template>
  <main class="bg-gradient-to-b from-[#1E2A78] via-[#6E1D67] to-[#160D2C] h-dvh w-dvw p-5">
    <RouterView />
  </main>
</template>
