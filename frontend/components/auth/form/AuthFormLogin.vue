<script setup lang="ts">
import type { FormField } from "~/types";

defineEmits(["openRegisterForm", "openPasswordRecoveryForm"]);

const { success } = useNotify();
const authStore = useAuthStore();

interface FeedbackForm {
  email: FormField<string>;
  password: FormField<string>;
  remember: FormField<boolean>;
}

const formData = reactive<FeedbackForm>({
  email: { value: "", error: "", required: true },
  password: { value: "", error: "", required: true },
  remember: { value: false, error: "", required: false },
});

const submitForm = async () => {
  console.log("submitForm", formData);

  try {
    await authStore.login(formData.email.value, formData.password.value);
    // modalsStore.closeModal("login");
    setTimeout(() => {
      success("Вы успешно авторизовались", 3000);
    }, 500);
  } catch (error) {
    console.log(error);
  }
};
</script>
<template>
  <div class="modal-login__wrapper">
    <div class="modal-login__header">
      <h3>Вход в аккаунт</h3>
      <p>Введите ваши данные для входа</p>
    </div>

    <form class="modal-login__form" @submit.prevent="submitForm">
      <BaseInput
        v-model:input-value="formData.email.value"
        v-model:error="formData.email.error"
        type="email"
        placeholder="Email"
        required
      />

      <BaseInput
        v-model:input-value="formData.password.value"
        v-model:error="formData.password.error"
        type="password"
        placeholder="Пароль"
        required
      />

      <div class="modal-login__options">
        <label class="modal-login__remember">
          <input v-model="formData.remember.value" type="checkbox" />
          <span>Запомнить меня</span>
        </label>
        <button
          type="button"
          class="modal-login__forgot"
          @click="$emit('openPasswordRecoveryForm')"
        >
          Забыли пароль?
        </button>
      </div>

      <BaseButton type="submit" size="lg" label="Войти" style="width: 100%" />

      <div class="modal-login__footer">
        <span>Ещё нет аккаунта?</span>
        <NuxtLink
          class="modal-login__footer-link"
          @click="$emit('openRegisterForm')"
        >
          Зарегистрироваться
        </NuxtLink>
      </div>
    </form>
  </div>
</template>
<style scoped lang="scss">
.modal-login {
  &__wrapper {
    position: relative;
    background: $bg;
    border-radius: 12px;
    padding: 40px 30px;
    box-shadow: 0 0 20px $white;
  }

  &__header {
    text-align: center;
    margin-bottom: 30px;

    h3 {
      color: $white;
      font-size: 1.8rem;
      margin-bottom: 8px;
    }

    p {
      color: rgba($white, 0.7);
      font-size: 0.9rem;
    }
  }

  &__form {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  &__options {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: -10px;
  }

  &__remember {
    display: flex;
    align-items: center;
    gap: 8px;
    color: rgba($white, 0.8);
    font-size: 0.9rem;
    cursor: pointer;

    input {
      accent-color: $accent;
    }
  }

  &__forgot {
    background: none;
    border: none;
    color: $accent;
    font-size: 0.9rem;
    cursor: pointer;
    padding: 5px;
  }

  &__submit {
    margin-top: 10px;
    background: $accent;
    color: $txt;
    font-weight: 600;
  }

  &__footer {
    text-align: center;
    margin-top: 20px;
    color: rgba($white, 0.7);
    font-size: 0.9rem;
    &-link {
      color: $accent;
      cursor: pointer;
    }

    button {
      background: none;
      border: none;
      color: $accent;
      cursor: pointer;
      margin-left: 5px;
      font-weight: 500;
    }
  }
}
</style>
