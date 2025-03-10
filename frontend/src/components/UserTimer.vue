<script setup lang="ts">
import { onMounted, onUnmounted, ref, computed, defineProps } from 'vue'
import { intervalToDuration } from 'date-fns'
import { getNextBirthday } from '@/utils'
import type { Duration } from 'date-fns'

const { first_name, last_name, username, birthday } = defineProps<{
  first_name: string
  last_name?: string
  username?: string
  birthday: Date
}>()

let intervalId: number | undefined = undefined
const now = ref<number>(new Date().getTime())
const nextBirthday = computed<Date | undefined>(() => {
  return getNextBirthday(birthday)
})
const duration = computed<Duration | undefined>(() => {
  if (nextBirthday.value === undefined) return undefined
  return intervalToDuration({ start: new Date(now.value), end: nextBirthday.value })
})

onMounted(() => {
  intervalId = setInterval(() => (now.value += 1000), 1000)
})

onUnmounted(() => {
  if (intervalId !== undefined) clearInterval(intervalId)
})
</script>

<template>
  <h3 class="text-xl text-center font-bold">Time to Birthday</h3>
  <h1 class="text-2xl font-bold text-center">{{ first_name }} {{ last_name }}</h1>
  <h2 class="text-xl text-center" v-if="username">@{{ username }}</h2>
  <div v-if="duration" class="flex flex-col items-center gap-4 mt-24">
    <div v-for="(value, key) in duration" :key="key" class="text-3xl">{{ value }} {{ key }}</div>
  </div>
</template>
