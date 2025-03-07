import { defineStore } from 'pinia'
import { formatISO } from 'date-fns'
import { ref } from 'vue'

interface UserData {
  first_name: string
  last_name?: string
  username?: string
  birthday: Date
}

const useUser = defineStore('user', () => {
  const token = window.Telegram.WebApp.initData
  const data = ref<UserData | null | undefined>(undefined)

  async function fetchUser() {
    const response = await fetch('http://192.168.31.220:8000/users/me', {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    })
    if (!response.ok) {
      data.value = null
    } else {
      const { birthday, ...rest } = await response.json()
      data.value = { ...rest, birthday: new Date(birthday) }
    }
  }

  async function register(date: Date): Promise<boolean> {
    const response = await fetch('http://192.168.31.220:8000/users', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ birthday: formatISO(date, { representation: 'date' }) }),
    })
    if (!response.ok) return false
    const { birthday, ...rest } = await response.json()
    data.value = { ...rest, birthday: new Date(birthday) }
    return true
  }

  return { token, data, fetch: fetchUser, register }
})

export default useUser
