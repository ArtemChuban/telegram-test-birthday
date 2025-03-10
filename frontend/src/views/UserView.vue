<script setup lang="ts">
import { ref, watch, onMounted, onUnmounted } from 'vue'
import useUser, { type UserData } from '@/stores/user'
import UserTimer from '@/components/UserTimer.vue'
import { useRoute } from 'vue-router'
import router from '@/router'
import LoaderSpinner from '@/components/LoaderSpinner.vue'

const route = useRoute()
const user = useUser()
const loading = ref<boolean>(false)
const data = ref<UserData | null | undefined>(undefined)
const error = ref<string | null>(null)

watch(
  () => route.params.id,
  (id) => fetchData(Number(id)),
  { immediate: true },
)

async function fetchData(id: number) {
  error.value = data.value = null
  loading.value = true
  try {
    data.value = await user.getUser(id)
    if (data.value === null) throw new Error('No user found')
  } catch (e) {
    error.value = (e as Error).toString()
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  window.Telegram.WebApp.BackButton.show().onClick(handleBackButtonClick)
})

onUnmounted(() => {
  window.Telegram.WebApp.BackButton.hide().offClick(handleBackButtonClick)
})

function handleBackButtonClick() {
  router.push('/')
}
</script>

<template>
  <div v-if="loading" class="flex justify-center">
    <LoaderSpinner />
  </div>
  <div v-else-if="error">{{ error }}</div>
  <UserTimer
    v-else-if="data"
    :first_name="data.first_name"
    :last_name="data.last_name"
    :username="data.username"
    :birthday="data.birthday"
  />
</template>
