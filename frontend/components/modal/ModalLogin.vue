<script lang="ts" setup>
import { api } from "~/api";
const modalsStore = useModalsStore();
const isClosing = ref(false);
const isSubmitting = ref(false);

const { $api } = useNuxtApp();

interface FormField<T> {
  value: T;
  error: string;
  required: boolean;
}

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

const handleAnimationEnd = () => {
  if (isClosing.value) {
    modalsStore.closeModal("login");
  }
};

// const submitForm = async () => {
//   isSubmitting.value = true;
//   try {
//     // Логика входа
//     await new Promise((resolve) => setTimeout(resolve, 1500));
//     modalsStore.closeModal("login");
//     useNotify().success("Вход выполнен успешно!");
//   } catch (error) {
//     useNotify().error("Ошибка входа. Проверьте данные");
//   } finally {
//     isSubmitting.value = false;
//   }
// };

const submitForm = async () => {
  console.log("submitForm", formData);

  try {
    const res = await $api(api.users.login, {
      method: "POST",
      body: {
        email: formData.email.value,
        password: formData.password.value,
      },
    });
    console.log(res);
  } catch (error) {
    console.log(error);
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
    class="modal-login"
    :class="{ 'modal-login_close': isClosing }"
    @animationend="handleAnimationEnd"
  >
    <div class="modal-login__wrapper">
      <BaseButtonClose
        top="10px"
        right="10px"
        :size="26"
        @click="modalsStore.closeModal('login')"
      />

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
          icon="email"
          required
        />

        <BaseInput
          v-model:input-value="formData.password.value"
          v-model:error="formData.password.error"
          type="password"
          placeholder="Пароль"
          icon="lock"
          required
        />

        <div class="modal-login__options">
          <!-- <label class="modal-login__remember">
            <input v-model="formData.remember.value" type="checkbox" />
            <span>Запомнить меня</span>
          </label> -->
          <BaseInputCheckbox
            v-model:agree-value="formData.remember.value"
            v-model:agree-error="formData.remember.error"
          >
           <span>Запомнить меня</span>
          </BaseInputCheckbox>
          <button
            type="button"
            class="modal-login__forgot"
            @click="openPasswordRecovery"
          >
            Забыли пароль?
          </button>
        </div>

        <BaseButton type="submit" size="lg" label="Войти" style="width: 100%" />

        <div class="modal-login__footer">
          <span>Ещё нет аккаунта?</span>
          <NuxtLink class="modal-login__footer-link" @click="openRegister">
            Зарегистрироваться
          </NuxtLink>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped lang="scss">
.modal-login {
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
    box-shadow: 0 0 20px #fff;
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
