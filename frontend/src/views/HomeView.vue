<script setup lang="ts">
import { onMounted, onUnmounted } from 'vue'
import { ref, computed, watch } from 'vue'
import { intervalToDuration } from 'date-fns'
import router from '@/router'
import useUser from '@/stores/user'
import { getNextBirthday } from '@/utils'
import type { Duration } from 'date-fns'

let intervalId: number | undefined = undefined
const user = useUser()
const now = ref<number>(new Date().getTime())
const nextBirthday = computed<Date | undefined>(() => {
  if (user.data === undefined || user.data === null) return undefined
  return getNextBirthday(user.data.birthday)
})
const duration = computed<Duration | undefined>(() => {
  if (nextBirthday.value === undefined) return undefined
  return intervalToDuration({ start: new Date(now.value), end: nextBirthday.value })
})

watch(
  () => user.data,
  (data) => {
    if (data === null) router.push('/input')
  },
)

onMounted(() => {
  intervalId = setInterval(() => (now.value += 1000), 1000)
})

onUnmounted(() => {
  if (intervalId !== undefined) clearInterval(intervalId)
})
</script>

<template>
  <template v-if="user.data">
    <h3 class="text-white text-xl text-center font-bold">Time to Birthday</h3>
    <h1 class="text-white text-2xl font-bold text-center">
      {{ user.data?.first_name }} {{ user.data?.last_name }}
    </h1>
    <h2 class="text-white text-xl text-center" v-if="user.data?.username">
      @{{ user.data.username }}
    </h2>
    <div v-if="duration" class="flex flex-col items-center gap-4 mt-24">
      <div v-for="(value, key) in duration" :key="key" class="text-white text-3xl">
        {{ value }} {{ key }}
      </div>
    </div>
  </template>
  <div v-else>Loading</div>
</template>
>
