<script setup lang="ts">
import { useAuth } from '#auth'

const auth = useAuth()

const form = reactive({
  username: '',
  password: '',
})

const error = ref('')

const submit = async () => {
  error.value = ''
  try {
    await auth.login('django-jwt', {
      data: {
        username: form.username,
        password: form.password,
      },
    })
    navigateTo('/')
  } catch (e: any) {
    error.value = e?.data?.detail || 'Ошибка входа'
  }
}
</script>

<template>
  <form @submit.prevent="submit">
    <input v-model="form.username" placeholder="Логин" required />
    <input v-model="form.password" type="password" placeholder="Пароль" required />
    <button type="submit">Войти</button>
    <p v-if="error" style="color:red">{{ error }}</p>
  </form>
</template>
