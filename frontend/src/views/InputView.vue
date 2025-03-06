<script setup lang="ts">
import "vue-scroll-picker/style.css";
import {
  format,
  setDate,
  setHours,
  setMinutes,
  setMonth,
  setSeconds,
  setYear,
} from 'date-fns'
import { computed, ref } from 'vue'
import { VueScrollPicker, VueScrollPickerValue } from 'vue-scroll-picker'
import ScrollPicker from 'vue3-scroll-picker';

const currentValue = ref(new Date())
const currentYear = computed(() => currentValue.value.getFullYear())
const currentMonth = computed(() => currentValue.value.getMonth() + 1)
const currentDay = computed(() => currentValue.value.getDate())

const years = computed(() => {
  const currYear = new Date().getFullYear()
  const lastYear = 1900
  return Array.from(
    { length: currYear - lastYear + 1 },
    (_, index) => lastYear + index,
  ).reverse()
})
const monthNames = [
  "Январь",
  "Февраль",
  "Март",
  "Апреля",
  "Май",
  "Июнь",
  "Июль",
  "Август",
  "Сентябрь",
  "Октябрь",
  "Ноябрь",
  "Декабрь",
]
const months = Array.from({ length: 12 }, (_, index) => { return { name: monthNames[index], value: index + 1 } })
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

function handleClick() {
  const date = format(currentValue.value, 'yyyy-MM-dd');
  console.log(date)
}
</script>

<template>
  <div class="flex flex-col justify-between h-full pb-5 gap-5">
    <h1 class="text-xl text-white font-bold text-center">Введите свою дату рождения</h1>
    <div class="picker-group">
      <VueScrollPicker :options="years" :model-value="currentYear" @update:model-value="handleUpdateYear" />
      <VueScrollPicker :options="months" :model-value="currentMonth" @update:model-value="handleUpdateMonth" />
      <VueScrollPicker :options="days" :model-value="currentDay" @update:model-value="handleUpdateDay" />
    </div>
    <button class="bg-white text-black rounded-xl w-full py-3 z-10" @click="handleClick">Продолжить</button>
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

.vue-scroll-picker-item[aria-selected=true] {
  color: white;
  opacity: 100%;
}

.vue-scroll-picker-layer-top,
.vue-scroll-picker-layer-bottom {
  background: transparent;
}
</style>
