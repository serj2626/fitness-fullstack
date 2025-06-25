<script lang="ts" setup>
const modalsStore = useModalsStore();
const isClosing = ref(false);
const isSubmitting = ref(false);

const formData = reactive({
  email: "",
  password: "",
  remember: false,
});

const closeModal = () => {
  isClosing.value = true;
};

const handleAnimationEnd = () => {
  if (isClosing.value) {
    modalsStore.closeModal("login");
  }
};

const submitForm = async () => {
  isSubmitting.value = true;
  try {
    // Логика входа
    await new Promise((resolve) => setTimeout(resolve, 1500));
    modalsStore.closeModal("login");
    useNotify().success("Вход выполнен успешно!");
  } catch (error) {
    useNotify().error("Ошибка входа. Проверьте данные");
  } finally {
    isSubmitting.value = false;
  }
};

const openRegister = () => {
  modalsStore.closeModal("login");
  modalsStore.openModal("register");
};

const openPasswordRecovery = () => {
  modalsStore.closeModal("login");
  modalsStore.openModal("passwordRecovery");
};
</script>

<template>
  <div
    class="auth-modal"
    :class="{ 'auth-modal_close': isClosing }"
    @animationend="handleAnimationEnd"
  >
    <div class="auth-modal__wrapper">
      <BaseButtonClose
        top="10px"
        right="10px"
        :size="26"
        @click="modalsStore.closeModal('login')"
      />

      <div class="auth-modal__header">
        <h3>Вход в аккаунт</h3>
        <p>Введите ваши данные для входа</p>
      </div>

      <form class="auth-modal__form" @submit.prevent="submitForm">
        <BaseInput
          v-model="formData.email"
          type="email"
          placeholder="Email"
          icon="email"
          required
        />

        <BaseInput
          v-model="formData.password"
          type="password"
          placeholder="Пароль"
          icon="lock"
          required
        />

        <div class="auth-modal__options">
          <label class="auth-modal__remember">
            <input v-model="formData.remember" type="checkbox" />
            <span>Запомнить меня</span>
          </label>
          <button
            type="button"
            class="auth-modal__forgot"
            @click="openPasswordRecovery"
          >
            Забыли пароль?
          </button>
        </div>

        <BaseButton
          type="submit"
          size="lg"
          label="Войти"
          style="width: 100%;"
        />

        <div class="auth-modal__footer">
          <span>Ещё нет аккаунта?</span>
          <button type="button" @click="openRegister">
            Зарегистрироваться
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped lang="scss">
.auth-modal {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  &__wrapper {
    position: relative;
    background: $bg;
    border-radius: 12px;
    padding: 40px 30px;
    width: 100%;
    max-width: 650px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
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

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
</style>
