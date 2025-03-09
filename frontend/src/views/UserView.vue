<script setup lang="ts">
import { onMounted, ref } from 'vue'
import useUser, { type UserData } from '@/stores/user'
import UserTimer from '@/components/UserTimer.vue'
import { useRoute } from 'vue-router'
const route = useRoute()

const user = useUser()
const data = ref<UserData | null | undefined>(undefined)
onMounted(async () => {
  // TODO: returns null if user not exist, show error message
  data.value = await user.getUser(Number(route.params.id))
})
</script>

<template>
  <UserTimer
    v-if="data"
    :first_name="data.first_name"
    :last_name="data.last_name"
    :username="data.username"
    :birthday="data.birthday"
  />
</template>
