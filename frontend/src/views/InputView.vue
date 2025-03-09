<script setup lang="ts">
import 'vue-scroll-picker/style.css'
import { setDate, setMonth, setYear } from 'date-fns'
import { onMounted, onUnmounted, computed, ref, watch } from 'vue'
import { VueScrollPicker, type VueScrollPickerValue } from 'vue-scroll-picker'
import router from '@/router'
import useUser from '@/stores/user'

const user = useUser()
const currentValue = ref(new Date())
const currentYear = computed(() => currentValue.value.getFullYear())
const currentMonth = computed(() => currentValue.value.getMonth() + 1)
const currentDay = computed(() => currentValue.value.getDate())

watch(
  () => user.data,
  (data) => {
    if (data) router.push('/')
  },
)

const years = computed(() => {
  const currYear = new Date().getFullYear()
  const lastYear = 1900
  return Array.from({ length: currYear - lastYear + 1 }, (_, index) => lastYear + index).reverse()
})
const monthNames = [
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  'November',
  'December',
]
const months = Array.from({ length: 12 }, (_, index) => {
  return { name: monthNames[index], value: index + 1 }
})
const days = computed(() => {
  const lastDay = new Date(currentYear.value, currentMonth.value, 0).getDate()
  return Array.from({ length: lastDay }, (_, index) => `${index + 1}`)
})

function handleUpdateYear(value: VueScrollPickerValue | undefined) {
  currentValue.value = setYear(currentValue.value, value as number)
}
function handleUpdateMonth(value: VueScrollPickerValue | undefined) {
  currentValue.value = setMonth(currentValue.value, (value as number) - 1)
}
function handleUpdateDay(value: VueScrollPickerValue | undefined) {
  currentValue.value = setDate(currentValue.value, value as number)
}

async function handleMainButtonClick() {
  const success = await user.register(currentValue.value)
  if (success) {
    router.push('/')
  }
}

onMounted(() => {
  window.Telegram.WebApp.MainButton.show()
    .enable()
    .setText('Continue')
    .onClick(handleMainButtonClick)
})

onUnmounted(() => {
  window.Telegram.WebApp.MainButton.hide().offClick(handleMainButtonClick)
})
</script>

<template>
  <div class="flex flex-col justify-between h-full pb-5 gap-5">
    <h1 class="text-xl text-white font-bold text-center">Enter your birthday date</h1>
    <div class="picker-group">
      <VueScrollPicker
        :options="years"
        :model-value="currentYear"
        @update:model-value="handleUpdateYear"
      />
      <VueScrollPicker
        :options="months"
        :model-value="currentMonth"
        @update:model-value="handleUpdateMonth"
      />
      <VueScrollPicker
        :options="days"
        :model-value="currentDay"
        @update:model-value="handleUpdateDay"
      />
    </div>
  </div>
</template>

<style>
.picker-group {
  display: flex;
  height: 100%;
}

.vue-scroll-picker {
  height: 100%;
}

.vue-scroll-picker-item {
  color: white;
  opacity: 50%;
}

.vue-scroll-picker-item[aria-selected='true'] {
  color: white;
  opacity: 100%;
}

.vue-scroll-picker-layer-top,
.vue-scroll-picker-layer-bottom {
  background: transparent;
}
</style>
