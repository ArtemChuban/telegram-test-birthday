<script setup lang="ts">
import { onMounted, onUnmounted, computed, watch } from 'vue'
import router from '@/router'
import useUser from '@/stores/user'
import UserTimer from '@/components/UserTimer.vue'
import LoaderSpinner from '@/components/LoaderSpinner.vue'

const user = useUser()
const shareUrl = computed<string>(() => {
  if (user.data === null || user.data === undefined) return ''
  return `https://t.me/share/url?url=${import.meta.env.VITE_WEB_APP_URL}?startapp=${user.data.id}&text=Look at how much time is left until my birthday`
})

watch(
  () => user.data,
  (data) => {
    if (data === null) router.push('/input')
  },
)

onMounted(() => {
  window.Telegram.WebApp.MainButton.show().enable().setText('Share').onClick(handleMainButtonClick)
  window.Telegram.WebApp.SecondaryButton.show()
    .enable()
    .setText('Edit')
    .onClick(handleSecondaryButtonClick)
})

onUnmounted(() => {
  window.Telegram.WebApp.MainButton.hide().offClick(handleMainButtonClick)
  window.Telegram.WebApp.SecondaryButton.hide().offClick(handleSecondaryButtonClick)
})

function handleMainButtonClick() {
  window.Telegram.WebApp.openTelegramLink(shareUrl.value)
}
function handleSecondaryButtonClick() {
  router.push('/input')
}
</script>

<template>
  <UserTimer
    v-if="user.data"
    :first_name="user.data.first_name"
    :last_name="user.data.last_name"
    :username="user.data.username"
    :birthday="user.data.birthday"
  />
  <div v-else class="flex justify-center">
    <LoaderSpinner />
  </div>
</template>
