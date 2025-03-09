import { defineStore } from 'pinia'
import { formatISO } from 'date-fns'
import { ref } from 'vue'

export interface UserData {
  id: number
  first_name: string
  last_name?: string
  username?: string
  birthday: Date
}

const useUser = defineStore('user', () => {
  const token = window.Telegram.WebApp.initData
  const data = ref<UserData | null | undefined>(undefined)

  async function fetchUser(): Promise<void> {
    const response = await fetch(`${import.meta.env.VITE_API_URL}/users/me`, {
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
    const response = await fetch(`${import.meta.env.VITE_API_URL}/users`, {
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

  async function getUser(userId: number): Promise<UserData | null> {
    const response = await fetch(`${import.meta.env.VITE_API_URL}/users/${userId}`, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    })
    if (!response.ok) return null
    const { birthday, ...rest } = await response.json()
    return { ...rest, birthday: new Date(birthday) }
  }

  return { token, data, fetch: fetchUser, register, getUser }
})

export default useUser
