import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import InputView from '../views/InputView.vue'
import UserView from '../views/UserView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/:id(\\d+)',
      name: 'user',
      component: UserView,
    },
    {
      path: '/input',
      name: 'input',
      component: InputView,
    },
  ],
})

export default router
