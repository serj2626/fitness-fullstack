<script setup lang="ts">
import { useAuth } from '#auth'
import { useAuthApi } from '~/composables/useAuthApi'

const auth = useAuth()
const { register } = useAuthApi()

const form = reactive({
  username: '',
  email: '',
  password: '',
  password2: '',
})

const error = ref('')

const submit = async () => {
  error.value = ''
  try {
    await register(form)
    await auth.login('django-jwt', {
      data: {
        username: form.username,
        password: form.password,
      },
    })
    navigateTo('/')
  } catch (e: any) {
    error.value = e?.data?.message || 'Ошибка регистрации'
  }
}
</script>

<template>
  <form @submit.prevent="submit">
    <input v-model="form.username" placeholder="Логин" required />
    <input v-model="form.email" type="email" placeholder="Email" required />
    <input v-model="form.password" type="password" placeholder="Пароль" required />
    <input v-model="form.password2" type="password" placeholder="Подтвердите пароль" required />
    <button type="submit">Зарегистрироваться</button>
    <p v-if="error" style="color:red">{{ error }}</p>
  </form>
</template>