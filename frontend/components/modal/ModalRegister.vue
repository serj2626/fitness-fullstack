<script lang="ts" setup>
const modalsStore = useModalsStore();
const isClosing = ref(false);
const isSubmitting = ref(false);

const formData = reactive({
  name: "",
  email: "",
  password: "",
  confirmPassword: "",
  agree: false,
});

const closeModal = () => {
  isClosing.value = true;
};

const handleAnimationEnd = () => {
  if (isClosing.value) {
    modalsStore.closeModal("register");
  }
};

const submitForm = async () => {
  if (formData.password !== formData.confirmPassword) {
    useNotify().error("Пароли не совпадают");
    return;
  }

  isSubmitting.value = true;
  try {
    // Логика регистрации
    await new Promise((resolve) => setTimeout(resolve, 1500));
    modalsStore.closeModal("register");
    useNotify().success("Регистрация прошла успешно!");
  } catch (error) {
    useNotify().error("Ошибка регистрации");
  } finally {
    isSubmitting.value = false;
  }
};

const openLogin = () => {
  modalsStore.closeModal("register");
  modalsStore.openModal("login");
};
</script>

<template>
  <div
    class="modal-register"
    :class="{ 'modal-register_close': isClosing }"
    @animationend="handleAnimationEnd"
  >
    <div class="modal-register__wrapper">
      <BaseButtonClose
        top="10px"
        right="10px"
        :size="26"
        @click="modalsStore.closeModal('register')"
      />

      <div class="modal-register__header">
        <h3>Создать аккаунт</h3>
        <p>Заполните форму для регистрации</p>
      </div>

      <form class="modal-register__form" @submit.prevent="submitForm">
        <BaseInput
          v-model="formData.name"
          placeholder="Ваше имя"
          icon="user"
          required
        />

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

        <BaseInput
          v-model="formData.confirmPassword"
          type="password"
          placeholder="Повторите пароль"
          icon="lock"
          required
        />

        <label class="modal-register__agree">
          <input v-model="formData.agree" type="checkbox" />
          <span
            >Я согласен с <a href="#">правилами</a> и
            <a href="#">политикой конфиденциальности</a></span
          >
        </label>

        <BaseButton
          type="submit"
          size="lg"
          :loading="isSubmitting"
          class="modal-register__submit"
          label="Зарегистрироваться"
        />

        <div class="modal-register__footer">
          <span>Уже есть аккаунт?</span>
          <button type="button" @click="openLogin">Войти</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped lang="scss">
.modal-register {
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
    max-width: 450px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  }

  &__close {
    position: absolute;
    top: 15px;
    right: 15px;
    background: none;
    border: none;
    color: $white;
    cursor: pointer;
    padding: 5px;
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

  &__agree {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    color: rgba($white, 0.8);
    font-size: 0.85rem;
    line-height: 1.4;
    cursor: pointer;
    margin-top: -10px;

    input {
      margin-top: 3px;
      accent-color: $accent;
      flex-shrink: 0;
    }

    a {
      color: $accent;
      text-decoration: none;

      &:hover {
        text-decoration: underline;
      }
    }
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
